// Full-page screenshots of ampy.se pages, mobile + desktop, consent pre-set,
// animations neutralized, opacity-hidden sections forced visible.
const { chromium } = require('playwright-core');
const path = require('path');

const OUT = path.join(__dirname, '..', 'data', 'screenshots');
const PAGES = [
  ['home', 'https://ampy.se/'],
  ['svc-elcentral', 'https://ampy.se/elservice/elcentral/'],
  ['svc-vitvaror', 'https://ampy.se/elservice/vitvaror/'],
  ['geo-elektriker-tyreso', 'https://ampy.se/elektriker/tyreso/'],
  ['geo-eljour-taby', 'https://ampy.se/eljour/taby/'],
  ['geo-elinstallation-vaxholm', 'https://ampy.se/elinstallation/vaxholm/'],
  ['geo-laddbox-nacka', 'https://ampy.se/laddbox/nacka/'],
  ['b2b-brf', 'https://ampy.se/bostadsrattsforening/'],
  ['prod-zaptec-go2', 'https://ampy.se/laddbox/zaptec-go-2/'],
  ['prod-sigenstor', 'https://ampy.se/solcellsbatterier/sigenstor/'],
  ['pillar-elektriker', 'https://ampy.se/elektriker/'],
  ['pillar-eljour', 'https://ampy.se/eljour/'],
  ['pillar-batterilagring', 'https://ampy.se/batterilagring/'],
  ['hub-laddboxar', 'https://ampy.se/laddboxar/'],
  ['om-oss', 'https://ampy.se/om-oss/'],
  ['kontakt', 'https://ampy.se/kontakt/'],
  ['artikel-elcentral', 'https://ampy.se/byta-elcentral-2026/'],
  ['magnet-energikalkylator', 'https://ampy.se/energikalkylator/'],
  ['thank-you', 'https://ampy.se/thank-you/'],
];

const VIEWPORTS = [
  ['mobile', { width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true }],
  ['desktop', { width: 1440, height: 900, deviceScaleFactor: 1.5, isMobile: false, hasTouch: false }],
];

(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  for (const [vpName, vp] of VIEWPORTS) {
    const ctx = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: vp.deviceScaleFactor,
      isMobile: vp.isMobile, hasTouch: vp.hasTouch,
      userAgent: vp.isMobile
        ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'
        : undefined,
      locale: 'sv-SE',
    });
    await ctx.addCookies([{
      name: 'ampy_consent',
      value: encodeURIComponent(JSON.stringify({ v: 1, t: Date.now(), c: { necessary: true, statistics: false, marketing: false } })),
      domain: 'ampy.se', path: '/',
    }]);
    for (const [slug, url] of PAGES) {
      const page = await ctx.newPage();
      try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
        await page.addStyleTag({ content: '*{animation:none!important;transition:none!important;scroll-behavior:auto!important}' });
        // trigger enterView by scrolling through the page
        await page.evaluate(async () => {
          const h = document.body.scrollHeight;
          for (let y = 0; y < h; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); }
          window.scrollTo(0, 0);
        });
        await page.waitForTimeout(1200);
        // force any still-hidden containers visible (the verified opacity:0 bug)
        await page.evaluate(() => {
          document.querySelectorAll('section, section *').forEach(el => {
            const cs = getComputedStyle(el);
            if (cs.opacity === '0') el.style.setProperty('opacity', '1', 'important');
          });
          // remove any leftover consent UI just in case
          document.querySelectorAll('[class*="consent"],[id*="consent"],[class*="cookie-banner"]').forEach(el => {
            if (el.getBoundingClientRect().height > 40) el.remove();
          });
        });
        await page.waitForTimeout(300);
        await page.screenshot({ path: `${OUT}/${slug}--${vpName}.png`, fullPage: true });
        console.log('ok', slug, vpName);
      } catch (e) {
        console.log('ERR', slug, vpName, e.message.slice(0, 120));
      }
      await page.close();
    }
    await ctx.close();
  }
  await browser.close();
})();
