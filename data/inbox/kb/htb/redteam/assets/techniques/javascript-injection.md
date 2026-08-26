

- inject css
```js

const injectCSS = css => {
  let el = document.createElement('style');
  el.type = 'text/css';
  el.innerText = css;
  document.head.appendChild(el);
  return el;pt
};
injectCSS('h1,h1:before{color:#ff0}h2,h2:before{color:#fd0}h3,h3:before{color:#fb0}h4,h4:before{color:#f90}h5,h5:before{color:#f70}h6,h6:before{color:#f50}h1:before{content:"1. "}h2:before{content:"2. "}h3:before{content:"3. "}h4:before{content:"4. "}h5:before{content:"5. "}h6:before{content:"6. "}');

```






- css
    - prefixed headings yellow getting darker
        - `h1,h1:before{color:#ff0}h2,h2:before{color:#fd0}h3,h3:before{color:#fb0}h4,h4:before{color:#f90}h5,h5:before{color:#f70}h6,h6:before{color:#f50}h1:before{content:"1. "}h2:before{content:"2. "}h3:before{content:"3. "}h4:before{content:"4. "}h5:before{content:"5. "}h6:before{content:"6. "}`