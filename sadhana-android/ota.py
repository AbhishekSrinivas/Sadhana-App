"""Splits the web layer into an app file and a small launcher so installed apps can update themselves.

www/index.html  (the app, as committed) becomes www/app.html with the build number added
www/index.html  becomes a launcher: opens a downloaded update if there is one, else app.html
www/version.json  build number, uploaded with every release so installed apps can find updates
"""
import json, os, sys
www = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www')
build = int(os.environ.get('BUILD_ID') or 1)
src = open(os.path.join(www, 'index.html'), encoding='utf-8').read()
t = '<title>Sadhana</title>'
if t not in src:
    sys.exit('title not found')
src = src.replace(t, t + '<script>window.SADHANA_BUILD=%d</script>' % build, 1)
open(os.path.join(www, 'app.html'), 'w', encoding='utf-8').write(src)
launcher = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Sadhana</title>
<style>html,body{margin:0;background:#1b1f2a}</style>
</head><body><script>
(function(){
var B=%d;
function run(){location.replace('app.html')}
try{
  var q=indexedDB.open('sadhana-ota',1);
  q.onupgradeneeded=function(){q.result.createObjectStore('f')};
  q.onerror=run;
  q.onsuccess=function(){try{
    var g=q.result.transaction('f').objectStore('f').get('app');
    g.onerror=run;
    g.onsuccess=function(){
      var a=g.result;
      if(!a||!a.html||a.build<=B){run();return}
      var tried=localStorage.getItem('sadhana-ota-try'),ok=localStorage.getItem('sadhana-ota-ok');
      if(tried==String(a.build)&&ok!=String(a.build)){
        try{q.result.transaction('f','readwrite').objectStore('f').delete('app')}catch(e){}
        run();return;
      }
      localStorage.setItem('sadhana-ota-try',String(a.build));
      document.open();document.write(a.html);document.close();
    };
  }catch(e){run()}};
}catch(e){run()}
})();
</script></body></html>
''' % build
open(os.path.join(www, 'index.html'), 'w', encoding='utf-8').write(launcher)
open(os.path.join(www, 'version.json'), 'w').write(json.dumps({'build': build}))
print('built build', build, 'app.html', len(src), 'bytes')
