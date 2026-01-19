const puppeteer = require('puppeteer');
const fs = require('fs');
const axeSource = require('axe-core').source;

(async () => {
  const url = process.argv[2] || 'https://lpi-test-jean-moulin-v3.vercel.app/';
  console.log('Launching browser...');
  const browser = await puppeteer.launch({args:['--no-sandbox','--disable-setuid-sandbox']});
  const page = await browser.newPage();
  console.log('Opening', url);
  await page.goto(url, {waitUntil: 'networkidle2', timeout: 60000});
  console.log('Injecting axe-core...');
  await page.addScriptTag({content: axeSource});
  console.log('Running axe...');
  const results = await page.evaluate(async () => {
    return await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa']}});
  });
  await browser.close();
  const out = '/tmp/axe_report.json';
  fs.writeFileSync(out, JSON.stringify(results, null, 2));
  console.log('Saved', out);
})();
