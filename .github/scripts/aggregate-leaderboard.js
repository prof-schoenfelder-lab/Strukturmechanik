const fs = require('fs');
const https = require('https');
const csvParse = require('csv-parse/lib/sync');

const configPath = process.env.CONFIG_PATH || 'docs/leaderboard-config.json';
if(!fs.existsSync(configPath)) { console.error('Config not found:', configPath); process.exit(1); }
const cfg = JSON.parse(fs.readFileSync(configPath, 'utf8'));
if(!cfg.csv_url) { console.error('csv_url missing in config'); process.exit(2); }

function fetchCsv(url){
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

(async function(){
  try{
    const csv = await fetchCsv(cfg.csv_url);
    const records = csvParse(csv, { columns: true, skip_empty_lines: true });
    const allTime = [];
    const today = [];
    records.forEach(r => {
      // try to parse fields flexibly
      const a = parseFloat(r['allTime'] || r['All-time'] || r['all_time'] || r['all']);
      const t = parseFloat(r['today'] || r['Today'] || r['today_points'] || r['today']);
      if(!isNaN(a)) allTime.push(a);
      if(!isNaN(t)) today.push(t);
    });
    const out = { allTime: allTime, today: today, maxPoints: cfg.maxPoints || null };
    if(!fs.existsSync('data')) fs.mkdirSync('data');
    fs.writeFileSync('data/leaderboard.json', JSON.stringify(out, null, 2));
    console.log('Wrote data/leaderboard.json');
  } catch(e){ console.error(e); process.exit(10); }
})();
