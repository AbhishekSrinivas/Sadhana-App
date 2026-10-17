<script>
/* Android app only: the system WebView has no speech synthesis, so route it to the phone's text-to-speech engine */
(function () {
  var C = window.Capacitor; if (!C || !C.isNativePlatform || !C.isNativePlatform()) return;
  var T; try { T = C.registerPlugin("TextToSpeech"); } catch (e) { return; }
  var voices = [{ lang: "hi-IN", name: "Hindi", default: true, localService: true, voiceURI: "hi-IN" }];
  try { T.getSupportedLanguages().then(function (r) { var l = (r && r.languages) || []; var v = []; l.forEach(function (x) { if (/^(sa|hi|mr|kn|ta|te|en)/i.test(x)) v.push({ lang: x, name: x, default: false, localService: true, voiceURI: x }); }); if (v.length) { voices.length = 0; v.forEach(function (x) { voices.push(x); }); } }).catch(function () {}); } catch (e) {}
  function U(t) { this.text = t; this.lang = ""; this.voice = null; this.rate = 1; this.pitch = 1; this.volume = 1; this.onend = null; this.onerror = null; }
  var synth = {
    speaking: false, pending: false, paused: false,
    getVoices: function () { return voices.slice(); },
    addEventListener: function () {}, removeEventListener: function () {},
    cancel: function () { try { T.stop().catch(function () {}); } catch (e) {} },
    speak: function (u) {
      var lang = (u.voice && u.voice.lang) || u.lang || "hi-IN";
      T.speak({ text: u.text, lang: lang, rate: u.rate || 1, pitch: u.pitch || 1, volume: 1, category: "ambient" })
        .then(function () { if (u.onend) u.onend({}); })
        .catch(function () { if (u.onerror) u.onerror({}); });
    }
  };
  try { Object.defineProperty(window, "SpeechSynthesisUtterance", { value: U, configurable: true, writable: true }); } catch (e) { window.SpeechSynthesisUtterance = U; }
  try { Object.defineProperty(window, "speechSynthesis", { value: synth, configurable: true }); } catch (e) { window.speechSynthesis = synth; }
})();
</script>
