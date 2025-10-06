// Bootstrap loader for inline tutorial embeds
document.addEventListener('DOMContentLoaded', () => {
  // wait until TutorialPlayer is available
  function tryInit(){
    if(!window.TutorialPlayer || typeof window.TutorialPlayer.init !== 'function'){
      // try again shortly
      setTimeout(tryInit, 120);
      return;
    }

    document.querySelectorAll('.tutorial-embed').forEach((el)=>{
      let src = el.dataset.tutorial;
      if(!src) return;

      // normalize src: strip leading/trailing slashes
      src = String(src).replace(/^\/+|\/+$/g, '');
      if(!src) return;
      const parts = src.split('/').filter(Boolean);

      // if an explicit JSON path is provided, use it directly
      let jsonUrl = null;
      if(src.endsWith('.json')){
        // accept both folder/imported.json and direct json file names
        jsonUrl = src.startsWith('/') ? src : ('/' + src);
      } else {
        // assume the last path part is the examples folder name
        const folder = parts.length ? parts[parts.length-1] : '';
        if(!folder) return;
  // prefer assets/tutorials path where player assets & tutorials live under docs/assets/tutorials
  jsonUrl = '/assets/tutorials/' + folder + '/imported.json';
      }

      // apply per-embed CSS overrides if provided
      if(el.dataset.height) el.style.setProperty('--tp-fixed-height', el.dataset.height);
      if(el.dataset.pillMinHeight) el.style.setProperty('--tp-pill-min-height', el.dataset.pillMinHeight);

      try{
        // pass a concrete jsonUrl so the player can load the JSON directly
        window.TutorialPlayer.init(el, { jsonUrl: jsonUrl });
      }catch(err){
        console.error('TutorialPlayer init failed for', src, err);
      }
    });
  }

  tryInit();
});
