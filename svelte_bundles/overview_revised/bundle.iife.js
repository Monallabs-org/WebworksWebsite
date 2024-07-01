var jpComponentBuilder=function(z){"use strict";var No=Object.defineProperty;var Po=(z,E,j)=>E in z?No(z,E,{enumerable:!0,configurable:!0,writable:!0,value:j}):z[E]=j;var st=(z,E,j)=>(Po(z,typeof E!="symbol"?E+"":E,j),j);function E(){}function j(e,t){for(const n in t)e[n]=t[n];return e}function rn(e){return e()}function on(){return Object.create(null)}function dt(e){e.forEach(rn)}function sn(e){return typeof e=="function"}function U(e,t){return e!=e?t==t:e!==t||e&&typeof e=="object"||typeof e=="function"}function Ma(e){return Object.keys(e).length===0}function ja(e,...t){if(e==null){for(const a of t)a(void 0);return E}const n=e.subscribe(...t);return n.unsubscribe?()=>n.unsubscribe():n}function Ut(e,t,n){e.$$.on_destroy.push(ja(t,n))}function fn(e){const t={};for(const n in e)n[0]!=="$"&&(t[n]=e[n]);return t}function ln(e,t){const n={};t=new Set(t);for(const a in e)!t.has(a)&&a[0]!=="$"&&(n[a]=e[a]);return n}function cn(e,t){e.appendChild(t)}function P(e,t,n){e.insertBefore(t,n||null)}function C(e){e.parentNode&&e.parentNode.removeChild(e)}function de(e,t){for(let n=0;n<e.length;n+=1)e[n]&&e[n].d(t)}function Wt(e){return document.createElement(e)}function ge(e){return document.createElementNS("http://www.w3.org/2000/svg",e)}function ve(e){return document.createTextNode(e)}function La(){return ve(" ")}function L(){return ve("")}function $(e,t,n,a){return e.addEventListener(t,n,a),()=>e.removeEventListener(t,n,a)}function Ra(e){return function(t){return t.preventDefault(),e.call(this,t)}}function Et(e,t,n){n==null?e.removeAttribute(t):e.getAttribute(t)!==n&&e.setAttribute(t,n)}const Fa=["width","height"];function za(e,t){const n=Object.getOwnPropertyDescriptors(e.__proto__);for(const a in t)t[a]==null?e.removeAttribute(a):a==="style"?e.style.cssText=t[a]:a==="__value"?e.value=e[a]=t[a]:n[a]&&n[a].set&&Fa.indexOf(a)===-1?e[a]=t[a]:Et(e,a,t[a])}function un(e,t){for(const n in t)Et(e,n,t[n])}function Da(e,t){Object.keys(t).forEach(n=>{Ya(e,n,t[n])})}function Ya(e,t,n){const a=t.toLowerCase();a in e?e[a]=typeof e[a]=="boolean"&&n===""?!0:n:t in e?e[t]=typeof e[t]=="boolean"&&n===""?!0:n:Et(e,t,n)}function mn(e){return/-/.test(e)?Da:za}function Ha(e){return Array.from(e.childNodes)}function Ua(e,t){t=""+t,e.data!==t&&(e.data=t)}class Wa{constructor(t=!1){st(this,"is_svg",!1);st(this,"e");st(this,"n");st(this,"t");st(this,"a");this.is_svg=t,this.e=this.n=null}c(t){this.h(t)}m(t,n,a=null){this.e||(this.is_svg?this.e=ge(n.nodeName):this.e=Wt(n.nodeType===11?"TEMPLATE":n.nodeName),this.t=n.tagName!=="TEMPLATE"?n:n.content,this.c(t)),this.i(a)}h(t){this.e.innerHTML=t,this.n=Array.from(this.e.nodeName==="TEMPLATE"?this.e.content.childNodes:this.e.childNodes)}i(t){for(let n=0;n<this.n.length;n+=1)P(this.t,this.n[n],t)}p(t){this.d(),this.h(t),this.i(this.a)}d(){this.n.forEach(C)}}function tt(e,t){return new e(t)}let pe;function St(e){pe=e}const gt=[],Ot=[];let vt=[];const be=[],Va=Promise.resolve();let he=!1;function Ba(){he||(he=!0,Va.then(dn))}function ye(e){vt.push(e)}function Ga(e){be.push(e)}const _e=new Set;let pt=0;function dn(){if(pt!==0)return;const e=pe;do{try{for(;pt<gt.length;){const t=gt[pt];pt++,St(t),Xa(t.$$)}}catch(t){throw gt.length=0,pt=0,t}for(St(null),gt.length=0,pt=0;Ot.length;)Ot.pop()();for(let t=0;t<vt.length;t+=1){const n=vt[t];_e.has(n)||(_e.add(n),n())}vt.length=0}while(gt.length);for(;be.length;)be.pop()();he=!1,_e.clear(),St(e)}function Xa(e){if(e.fragment!==null){e.update(),dt(e.before_update);const t=e.dirty;e.dirty=[-1],e.fragment&&e.fragment.p(e.ctx,t),e.after_update.forEach(ye)}}function qa(e){const t=[],n=[];vt.forEach(a=>e.indexOf(a)===-1?t.push(a):n.push(a)),n.forEach(a=>a()),vt=t}const Vt=new Set;let ft;function W(){ft={r:0,c:[],p:ft}}function V(){ft.r||dt(ft.c),ft=ft.p}function _(e,t){e&&e.i&&(Vt.delete(e),e.i(t))}function k(e,t,n,a){if(e&&e.o){if(Vt.has(e))return;Vt.add(e),ft.c.push(()=>{Vt.delete(e),a&&(n&&e.d(1),a())}),e.o(t)}else a&&a()}function bt(e){return(e==null?void 0:e.length)!==void 0?e:Array.from(e)}function Ct(e,t){const n={},a={},r={$$scope:1};let o=e.length;for(;o--;){const i=e[o],s=t[o];if(s){for(const f in i)f in s||(a[f]=1);for(const f in s)r[f]||(n[f]=s[f],r[f]=1);e[o]=s}else for(const f in i)r[f]=1}for(const i in a)i in n||(n[i]=void 0);return n}function Bt(e){return typeof e=="object"&&e!==null?e:{}}function Ka(e,t,n){const a=e.$$.props[t];a!==void 0&&(e.$$.bound[a]=n,n(e.$$.ctx[a]))}function D(e){e&&e.c()}function R(e,t,n){const{fragment:a,after_update:r}=e.$$;a&&a.m(t,n),ye(()=>{const o=e.$$.on_mount.map(rn).filter(sn);e.$$.on_destroy?e.$$.on_destroy.push(...o):dt(o),e.$$.on_mount=[]}),r.forEach(ye)}function F(e,t){const n=e.$$;n.fragment!==null&&(qa(n.after_update),dt(n.on_destroy),n.fragment&&n.fragment.d(t),n.on_destroy=n.fragment=null,n.ctx=[])}function Ja(e,t){e.$$.dirty[0]===-1&&(gt.push(e),Ba(),e.$$.dirty.fill(0)),e.$$.dirty[t/31|0]|=1<<t%31}function et(e,t,n,a,r,o,i=null,s=[-1]){const f=pe;St(e);const l=e.$$={fragment:null,ctx:[],props:o,update:E,not_equal:r,bound:on(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(t.context||(f?f.$$.context:[])),callbacks:on(),dirty:s,skip_bound:!1,root:t.target||f.$$.root};i&&i(l.root);let u=!1;if(l.ctx=n?n(e,t.props||{},(c,p,...h)=>{const m=h.length?h[0]:p;return l.ctx&&r(l.ctx[c],l.ctx[c]=m)&&(!l.skip_bound&&l.bound[c]&&l.bound[c](m),u&&Ja(e,c)),p}):[],l.update(),u=!0,dt(l.before_update),l.fragment=a?a(l.ctx):!1,t.target){if(t.hydrate){const c=Ha(t.target);l.fragment&&l.fragment.l(c),c.forEach(C)}else l.fragment&&l.fragment.c();t.intro&&_(e.$$.fragment),R(e,t.target,t.anchor),dn()}St(f)}class nt{constructor(){st(this,"$$");st(this,"$$set")}$destroy(){F(this,1),this.$destroy=E}$on(t,n){if(!sn(n))return E;const a=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return a.push(n),()=>{const r=a.indexOf(n);r!==-1&&a.splice(r,1)}}$set(t){this.$$set&&!Ma(t)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}const Qa="4";typeof window<"u"&&(window.__svelte||(window.__svelte={v:new Set})).v.add(Qa);const ht=[];function ke(e,t){return{subscribe:we(e,t).subscribe}}function we(e,t=E){let n;const a=new Set;function r(s){if(U(e,s)&&(e=s,n)){const f=!ht.length;for(const l of a)l[1](),ht.push(l,e);if(f){for(let l=0;l<ht.length;l+=2)ht[l][0](ht[l+1]);ht.length=0}}}function o(s){r(s(e))}function i(s,f=E){const l=[s,f];return a.add(l),a.size===1&&(n=t(r,o)||E),s(e),()=>{a.delete(l),a.size===0&&n&&(n(),n=null)}}return{set:r,update:o,subscribe:i}}const gn=we({});let Gt={};function Za(){console.log("initMapStore called"),gn.set(Gt)}function $a(e,t){Gt[e]=t,gn.set(Gt)}function tr(e,t){Gt[e].updateTwClass(t)}function vn(e,t,n){const a=e.slice();return a[9]=t[n],a}function pn(e){let t=e[0].text+"",n;return{c(){n=ve(t)},m(a,r){P(a,n,r)},p(a,r){r&1&&t!==(t=a[0].text+"")&&Ua(n,t)},d(a){a&&C(n)}}}function bn(e){let t,n,a;var r=ue;function o(i,s){return{props:{jp_props:i[9]}}}return r&&(t=tt(r,o(e))),{c(){t&&D(t.$$.fragment),n=L()},m(i,s){t&&R(t,i,s),P(i,n,s),a=!0},p(i,s){if(r!==(r=ue)){if(t){W();const f=t;k(f.$$.fragment,1,0,()=>{F(f,1)}),V()}r?(t=tt(r,o(i)),D(t.$$.fragment),_(t.$$.fragment,1),R(t,n.parentNode,n)):t=null}else if(r){const f={};s&1&&(f.jp_props=i[9]),t.$set(f)}},i(i){a||(t&&_(t.$$.fragment,i),a=!0)},o(i){t&&k(t.$$.fragment,i),a=!1},d(i){i&&C(n),t&&F(t,i)}}}function hn(e){let t,n,a=e[9].show&&bn(e);return{c(){a&&a.c(),t=L()},m(r,o){a&&a.m(r,o),P(r,t,o),n=!0},p(r,o){r[9].show?a?(a.p(r,o),o&1&&_(a,1)):(a=bn(r),a.c(),_(a,1),a.m(t.parentNode,t)):a&&(W(),k(a,1,1,()=>{a=null}),V())},i(r){n||(_(a),n=!0)},o(r){k(a),n=!1},d(r){r&&C(t),a&&a.d(r)}}}function yn(e){let t,n=e[0].inner_html+"",a;return{c(){t=new Wa(!1),a=L(),t.a=a},m(r,o){t.m(n,r,o),P(r,a,o)},p(r,o){o&1&&n!==(n=r[0].inner_html+"")&&t.p(n)},d(r){r&&(C(a),t.d())}}}function xe(e){let t,n,a,r,o,i,s=e[0].text&&pn(e),f=bt(e[0].object_props),l=[];for(let m=0;m<f.length;m+=1)l[m]=hn(vn(e,f,m));const u=m=>k(l[m],1,1,()=>{l[m]=null});let c=e[0].inner_html&&yn(e),p=[e[1]],h={};for(let m=0;m<p.length;m+=1)h=j(h,p[m]);return{c(){t=Wt(e[0].html_tag),s&&s.c(),n=L();for(let m=0;m<l.length;m+=1)l[m].c();a=L(),c&&c.c(),mn(e[0].html_tag)(t,h)},m(m,y){P(m,t,y),s&&s.m(t,null),cn(t,n);for(let b=0;b<l.length;b+=1)l[b]&&l[b].m(t,null);cn(t,a),c&&c.m(t,null),r=!0,o||(i=[$(t,"click",e[2].click),$(t,"change",e[2].change),$(t,"submit",Ra(e[2].submit)),$(t,"mouseover",e[2].mouseover),$(t,"mouseenter",e[2].mouseenter),$(t,"mouseleave",e[2].mouseleave),$(t,"mouseout",e[2].mouseout),$(t,"dblclick",e[2].dblclick)],o=!0)},p(m,y){if(m[0].text?s?s.p(m,y):(s=pn(m),s.c(),s.m(t,n)):s&&(s.d(1),s=null),y&1){f=bt(m[0].object_props);let b;for(b=0;b<f.length;b+=1){const S=vn(m,f,b);l[b]?(l[b].p(S,y),_(l[b],1)):(l[b]=hn(S),l[b].c(),_(l[b],1),l[b].m(t,a))}for(W(),b=f.length;b<l.length;b+=1)u(b);V()}m[0].inner_html?c?c.p(m,y):(c=yn(m),c.c(),c.m(t,null)):c&&(c.d(1),c=null),mn(m[0].html_tag)(t,h=Ct(p,[y&2&&m[1]]))},i(m){if(!r){for(let y=0;y<f.length;y+=1)_(l[y]);r=!0}},o(m){l=l.filter(Boolean);for(let y=0;y<l.length;y+=1)k(l[y]);r=!1},d(m){m&&C(t),s&&s.d(),de(l,m),c&&c.d(),o=!1,dt(i)}}}function er(e){let t=e[0].html_tag,n,a=e[0].html_tag&&xe(e);return{c(){a&&a.c(),n=L()},m(r,o){a&&a.m(r,o),P(r,n,o)},p(r,[o]){r[0].html_tag?t?U(t,r[0].html_tag)?(a.d(1),a=xe(r),t=r[0].html_tag,a.c(),a.m(n.parentNode,n)):a.p(r,o):(a=xe(r),t=r[0].html_tag,a.c(),a.m(n.parentNode,n)):t&&(a.d(1),a=null,t=r[0].html_tag)},i:E,o(r){k(a,r)},d(r){r&&C(n),a&&a.d(r)}}}function nr(e,t,n){let a,{jp_props:r}=t,{comp_ref:o}=t,{props:i={}}=t,s;i.jp_props=r;function f(c){return function(p){r.events.includes(c)&&eventHandler_CSR(i,p,!1)}}const l={click:f("click"),change:f("change"),submit:f("submit"),mouseover:f("mouseover"),mouseenter:f("mouseenter"),mouseleave:f("mouseleave"),mouseout:f("mouseout"),dblclick:f("dblclick")};function u(c){n(1,a.class=c,a)}return e.$$set=c=>{"jp_props"in c&&n(0,r=c.jp_props),"comp_ref"in c&&n(4,o=c.comp_ref),"props"in c&&n(3,i=c.props)},e.$$.update=()=>{e.$$.dirty&17&&o&&r.id!==void 0&&n(6,s=o),e.$$.dirty&81&&o&&r.id!==void 0&&$a(r.id,s),e.$$.dirty&1&&n(1,a={...r.attrs,style:r.style,class:r.classes})},[r,a,l,i,o,u,s]}class _n extends nt{constructor(t){super(),et(this,t,nr,er,U,{jp_props:0,comp_ref:4,props:3,updateTwClass:5})}get updateTwClass(){return this.$$.ctx[5]}}function kn(e,t,n){const a=e.slice();return a[3]=t[n],a}function ar(e){let t,n,a;var r=e[2][e[3].vue_type];function o(i,s){return{props:{jp_props:i[3]}}}return r&&(t=tt(r,o(e))),{c(){t&&D(t.$$.fragment),n=L()},m(i,s){t&&R(t,i,s),P(i,n,s),a=!0},p(i,s){if(s&1&&r!==(r=i[2][i[3].vue_type])){if(t){W();const f=t;k(f.$$.fragment,1,0,()=>{F(f,1)}),V()}r?(t=tt(r,o(i)),D(t.$$.fragment),_(t.$$.fragment,1),R(t,n.parentNode,n)):t=null}else if(r){const f={};s&1&&(f.jp_props=i[3]),t.$set(f)}},i(i){a||(t&&_(t.$$.fragment,i),a=!0)},o(i){t&&k(t.$$.fragment,i),a=!1},d(i){i&&C(n),t&&F(t,i)}}}function rr(e){let t,n;return t=new xn({props:{jp_props:e[3]}}),{c(){D(t.$$.fragment)},m(a,r){R(t,a,r),n=!0},p(a,r){const o={};r&1&&(o.jp_props=a[3]),t.$set(o)},i(a){n||(_(t.$$.fragment,a),n=!0)},o(a){k(t.$$.fragment,a),n=!1},d(a){F(t,a)}}}function wn(e){let t,n,a,r;const o=[rr,ar],i=[];function s(f,l){return f[3].vue_type==="svg_component"?0:1}return t=s(e),n=i[t]=o[t](e),{c(){n.c(),a=L()},m(f,l){i[t].m(f,l),P(f,a,l),r=!0},p(f,l){let u=t;t=s(f),t===u?i[t].p(f,l):(W(),k(i[u],1,1,()=>{i[u]=null}),V(),n=i[t],n?n.p(f,l):(n=i[t]=o[t](f),n.c()),_(n,1),n.m(a.parentNode,a))},i(f){r||(_(n),r=!0)},o(f){k(n),r=!1},d(f){f&&C(a),i[t].d(f)}}}function Ae(e){let t,n,a=bt(e[0].object_props),r=[];for(let i=0;i<a.length;i+=1)r[i]=wn(kn(e,a,i));const o=i=>k(r[i],1,1,()=>{r[i]=null});return{c(){t=ge(e[0].html_tag);for(let i=0;i<r.length;i+=1)r[i].c();un(t,{...e[1]})},m(i,s){P(i,t,s);for(let f=0;f<r.length;f+=1)r[f]&&r[f].m(t,null);n=!0},p(i,s){if(s&5){a=bt(i[0].object_props);let f;for(f=0;f<a.length;f+=1){const l=kn(i,a,f);r[f]?(r[f].p(l,s),_(r[f],1)):(r[f]=wn(l),r[f].c(),_(r[f],1),r[f].m(t,null))}for(W(),f=a.length;f<r.length;f+=1)o(f);V()}},i(i){if(!n){for(let s=0;s<a.length;s+=1)_(r[s]);n=!0}},o(i){r=r.filter(Boolean);for(let s=0;s<r.length;s+=1)k(r[s]);n=!1},d(i){i&&C(t),de(r,i)}}}function ir(e){let t=e[0].html_tag,n,a=e[0].html_tag&&Ae(e);return{c(){a&&a.c(),n=L()},m(r,o){a&&a.m(r,o),P(r,n,o)},p(r,[o]){r[0].html_tag?t?U(t,r[0].html_tag)?(a.d(1),a=Ae(r),t=r[0].html_tag,a.c(),a.m(n.parentNode,n)):a.p(r,o):(a=Ae(r),t=r[0].html_tag,a.c(),a.m(n.parentNode,n)):t&&(a.d(1),a=null,t=r[0].html_tag)},i:E,o(r){k(a,r)},d(r){r&&C(n),a&&a.d(r)}}}function or(e,t,n){let{jp_props:a}=t;const r={...a.attrs,class:a.classes};let o={html_component:_n};return e.$$set=i=>{"jp_props"in i&&n(0,a=i.jp_props)},[a,r,o]}class xn extends nt{constructor(t){super(),et(this,t,or,ir,U,{jp_props:0})}}function sr(e){const{beat:t,fade:n,beatFade:a,bounce:r,shake:o,flash:i,spin:s,spinPulse:f,spinReverse:l,pulse:u,fixedWidth:c,inverse:p,border:h,listItem:m,flip:y,size:b,rotation:S,pull:w}=e,N={"fa-beat":t,"fa-fade":n,"fa-beat-fade":a,"fa-bounce":r,"fa-shake":o,"fa-flash":i,"fa-spin":s,"fa-spin-reverse":l,"fa-spin-pulse":f,"fa-pulse":u,"fa-fw":c,"fa-inverse":p,"fa-border":h,"fa-li":m,"fa-flip":y===!0,"fa-flip-horizontal":y==="horizontal"||y==="both","fa-flip-vertical":y==="vertical"||y==="both",[`fa-${b}`]:typeof b<"u"&&b!==null,[`fa-rotate-${S}`]:typeof S<"u"&&S!==null&&S!==0,[`fa-pull-${w}`]:typeof w<"u"&&w!==null,"fa-swap-opacity":e.swapOpacity};return Object.keys(N).map(T=>N[T]?T:null).filter(T=>T)}function fr(e){return e=e-0,e===e}function lr(e){return fr(e)?e:(e=e.replace(/[\-_\s]+(.)?/g,function(t,n){return n?n.toUpperCase():""}),e.substr(0,1).toLowerCase()+e.substr(1))}function cr(e){return typeof e=="string"?e:Object.keys(e).reduce((t,n)=>t+n.split(/(?=[A-Z])/).join("-").toLowerCase()+":"+e[n]+";","")}function An(e,t,n={}){if(typeof t=="string")return t;const a=(t.children||[]).map(o=>An(e,o)),r=Object.keys(t.attributes||{}).reduce((o,i)=>{const s=t.attributes[i];return i==="style"?o.attrs.style=cr(s):i.indexOf("aria-")===0||i.indexOf("data-")===0?o.attrs[i.toLowerCase()]=s:o.attrs[lr(i)]=s,o},{attrs:{}});return e(t.tag,{...r.attrs},a)}function En(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter(function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable})),n.push.apply(n,a)}return n}function d(e){for(var t=1;t<arguments.length;t++){var n=arguments[t]!=null?arguments[t]:{};t%2?En(Object(n),!0).forEach(function(a){I(e,a,n[a])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):En(Object(n)).forEach(function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(n,a))})}return e}function Xt(e){"@babel/helpers - typeof";return Xt=typeof Symbol=="function"&&typeof Symbol.iterator=="symbol"?function(t){return typeof t}:function(t){return t&&typeof Symbol=="function"&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},Xt(e)}function ur(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function Sn(e,t){for(var n=0;n<t.length;n++){var a=t[n];a.enumerable=a.enumerable||!1,a.configurable=!0,"value"in a&&(a.writable=!0),Object.defineProperty(e,a.key,a)}}function mr(e,t,n){return t&&Sn(e.prototype,t),n&&Sn(e,n),Object.defineProperty(e,"prototype",{writable:!1}),e}function I(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function Ee(e,t){return gr(e)||pr(e,t)||On(e,t)||hr()}function Nt(e){return dr(e)||vr(e)||On(e)||br()}function dr(e){if(Array.isArray(e))return Se(e)}function gr(e){if(Array.isArray(e))return e}function vr(e){if(typeof Symbol<"u"&&e[Symbol.iterator]!=null||e["@@iterator"]!=null)return Array.from(e)}function pr(e,t){var n=e==null?null:typeof Symbol<"u"&&e[Symbol.iterator]||e["@@iterator"];if(n!=null){var a=[],r=!0,o=!1,i,s;try{for(n=n.call(e);!(r=(i=n.next()).done)&&(a.push(i.value),!(t&&a.length===t));r=!0);}catch(f){o=!0,s=f}finally{try{!r&&n.return!=null&&n.return()}finally{if(o)throw s}}return a}}function On(e,t){if(e){if(typeof e=="string")return Se(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);if(n==="Object"&&e.constructor&&(n=e.constructor.name),n==="Map"||n==="Set")return Array.from(e);if(n==="Arguments"||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return Se(e,t)}}function Se(e,t){(t==null||t>e.length)&&(t=e.length);for(var n=0,a=new Array(t);n<t;n++)a[n]=e[n];return a}function br(){throw new TypeError(`Invalid attempt to spread non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}function hr(){throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`)}var Cn=function(){},Oe={},Nn={},Pn=null,In={mark:Cn,measure:Cn};try{typeof window<"u"&&(Oe=window),typeof document<"u"&&(Nn=document),typeof MutationObserver<"u"&&(Pn=MutationObserver),typeof performance<"u"&&(In=performance)}catch{}var yr=Oe.navigator||{},Tn=yr.userAgent,Mn=Tn===void 0?"":Tn,at=Oe,x=Nn,jn=Pn,qt=In;at.document;var K=!!x.documentElement&&!!x.head&&typeof x.addEventListener=="function"&&typeof x.createElement=="function",Ln=~Mn.indexOf("MSIE")||~Mn.indexOf("Trident/"),Kt,Jt,Qt,Zt,$t,J="___FONT_AWESOME___",Ce=16,Rn="fa",Fn="svg-inline--fa",lt="data-fa-i2svg",Ne="data-fa-pseudo-element",_r="data-fa-pseudo-element-pending",Pe="data-prefix",Ie="data-icon",zn="fontawesome-i2svg",kr="async",wr=["HTML","HEAD","STYLE","SCRIPT"],Dn=function(){try{return process.env.NODE_ENV==="production"}catch{return!1}}(),A="classic",O="sharp",Te=[A,O];function Pt(e){return new Proxy(e,{get:function(n,a){return a in n?n[a]:n[A]}})}var It=Pt((Kt={},I(Kt,A,{fa:"solid",fas:"solid","fa-solid":"solid",far:"regular","fa-regular":"regular",fal:"light","fa-light":"light",fat:"thin","fa-thin":"thin",fad:"duotone","fa-duotone":"duotone",fab:"brands","fa-brands":"brands",fak:"kit",fakd:"kit","fa-kit":"kit","fa-kit-duotone":"kit"}),I(Kt,O,{fa:"solid",fass:"solid","fa-solid":"solid",fasr:"regular","fa-regular":"regular",fasl:"light","fa-light":"light",fast:"thin","fa-thin":"thin"}),Kt)),Tt=Pt((Jt={},I(Jt,A,{solid:"fas",regular:"far",light:"fal",thin:"fat",duotone:"fad",brands:"fab",kit:"fak"}),I(Jt,O,{solid:"fass",regular:"fasr",light:"fasl",thin:"fast"}),Jt)),Mt=Pt((Qt={},I(Qt,A,{fab:"fa-brands",fad:"fa-duotone",fak:"fa-kit",fal:"fa-light",far:"fa-regular",fas:"fa-solid",fat:"fa-thin"}),I(Qt,O,{fass:"fa-solid",fasr:"fa-regular",fasl:"fa-light",fast:"fa-thin"}),Qt)),xr=Pt((Zt={},I(Zt,A,{"fa-brands":"fab","fa-duotone":"fad","fa-kit":"fak","fa-light":"fal","fa-regular":"far","fa-solid":"fas","fa-thin":"fat"}),I(Zt,O,{"fa-solid":"fass","fa-regular":"fasr","fa-light":"fasl","fa-thin":"fast"}),Zt)),Ar=/fa(s|r|l|t|d|b|k|ss|sr|sl|st)?[\-\ ]/,Yn="fa-layers-text",Er=/Font ?Awesome ?([56 ]*)(Solid|Regular|Light|Thin|Duotone|Brands|Free|Pro|Sharp|Kit)?.*/i,Sr=Pt(($t={},I($t,A,{900:"fas",400:"far",normal:"far",300:"fal",100:"fat"}),I($t,O,{900:"fass",400:"fasr",300:"fasl",100:"fast"}),$t)),Hn=[1,2,3,4,5,6,7,8,9,10],Or=Hn.concat([11,12,13,14,15,16,17,18,19,20]),Cr=["class","data-prefix","data-icon","data-fa-transform","data-fa-mask"],ct={GROUP:"duotone-group",SWAP_OPACITY:"swap-opacity",PRIMARY:"primary",SECONDARY:"secondary"},jt=new Set;Object.keys(Tt[A]).map(jt.add.bind(jt)),Object.keys(Tt[O]).map(jt.add.bind(jt));var Nr=[].concat(Te,Nt(jt),["2xs","xs","sm","lg","xl","2xl","beat","border","fade","beat-fade","bounce","flip-both","flip-horizontal","flip-vertical","flip","fw","inverse","layers-counter","layers-text","layers","li","pull-left","pull-right","pulse","rotate-180","rotate-270","rotate-90","rotate-by","shake","spin-pulse","spin-reverse","spin","stack-1x","stack-2x","stack","ul",ct.GROUP,ct.SWAP_OPACITY,ct.PRIMARY,ct.SECONDARY]).concat(Hn.map(function(e){return"".concat(e,"x")})).concat(Or.map(function(e){return"w-".concat(e)})),Lt=at.FontAwesomeConfig||{};function Pr(e){var t=x.querySelector("script["+e+"]");if(t)return t.getAttribute(e)}function Ir(e){return e===""?!0:e==="false"?!1:e==="true"?!0:e}if(x&&typeof x.querySelector=="function"){var Tr=[["data-family-prefix","familyPrefix"],["data-css-prefix","cssPrefix"],["data-family-default","familyDefault"],["data-style-default","styleDefault"],["data-replacement-class","replacementClass"],["data-auto-replace-svg","autoReplaceSvg"],["data-auto-add-css","autoAddCss"],["data-auto-a11y","autoA11y"],["data-search-pseudo-elements","searchPseudoElements"],["data-observe-mutations","observeMutations"],["data-mutate-approach","mutateApproach"],["data-keep-original-source","keepOriginalSource"],["data-measure-performance","measurePerformance"],["data-show-missing-icons","showMissingIcons"]];Tr.forEach(function(e){var t=Ee(e,2),n=t[0],a=t[1],r=Ir(Pr(n));r!=null&&(Lt[a]=r)})}var Un={styleDefault:"solid",familyDefault:"classic",cssPrefix:Rn,replacementClass:Fn,autoReplaceSvg:!0,autoAddCss:!0,autoA11y:!0,searchPseudoElements:!1,observeMutations:!0,mutateApproach:"async",keepOriginalSource:!0,measurePerformance:!1,showMissingIcons:!0};Lt.familyPrefix&&(Lt.cssPrefix=Lt.familyPrefix);var yt=d(d({},Un),Lt);yt.autoReplaceSvg||(yt.observeMutations=!1);var g={};Object.keys(Un).forEach(function(e){Object.defineProperty(g,e,{enumerable:!0,set:function(n){yt[e]=n,Rt.forEach(function(a){return a(g)})},get:function(){return yt[e]}})}),Object.defineProperty(g,"familyPrefix",{enumerable:!0,set:function(t){yt.cssPrefix=t,Rt.forEach(function(n){return n(g)})},get:function(){return yt.cssPrefix}}),at.FontAwesomeConfig=g;var Rt=[];function Mr(e){return Rt.push(e),function(){Rt.splice(Rt.indexOf(e),1)}}var rt=Ce,G={size:16,x:0,y:0,rotate:0,flipX:!1,flipY:!1};function jr(e){if(!(!e||!K)){var t=x.createElement("style");t.setAttribute("type","text/css"),t.innerHTML=e;for(var n=x.head.childNodes,a=null,r=n.length-1;r>-1;r--){var o=n[r],i=(o.tagName||"").toUpperCase();["STYLE","LINK"].indexOf(i)>-1&&(a=o)}return x.head.insertBefore(t,a),e}}var Lr="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";function Ft(){for(var e=12,t="";e-- >0;)t+=Lr[Math.random()*62|0];return t}function _t(e){for(var t=[],n=(e||[]).length>>>0;n--;)t[n]=e[n];return t}function Me(e){return e.classList?_t(e.classList):(e.getAttribute("class")||"").split(" ").filter(function(t){return t})}function Wn(e){return"".concat(e).replace(/&/g,"&amp;").replace(/"/g,"&quot;").replace(/'/g,"&#39;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}function Rr(e){return Object.keys(e||{}).reduce(function(t,n){return t+"".concat(n,'="').concat(Wn(e[n]),'" ')},"").trim()}function te(e){return Object.keys(e||{}).reduce(function(t,n){return t+"".concat(n,": ").concat(e[n].trim(),";")},"")}function je(e){return e.size!==G.size||e.x!==G.x||e.y!==G.y||e.rotate!==G.rotate||e.flipX||e.flipY}function Fr(e){var t=e.transform,n=e.containerWidth,a=e.iconWidth,r={transform:"translate(".concat(n/2," 256)")},o="translate(".concat(t.x*32,", ").concat(t.y*32,") "),i="scale(".concat(t.size/16*(t.flipX?-1:1),", ").concat(t.size/16*(t.flipY?-1:1),") "),s="rotate(".concat(t.rotate," 0 0)"),f={transform:"".concat(o," ").concat(i," ").concat(s)},l={transform:"translate(".concat(a/2*-1," -256)")};return{outer:r,inner:f,path:l}}function zr(e){var t=e.transform,n=e.width,a=n===void 0?Ce:n,r=e.height,o=r===void 0?Ce:r,i=e.startCentered,s=i===void 0?!1:i,f="";return s&&Ln?f+="translate(".concat(t.x/rt-a/2,"em, ").concat(t.y/rt-o/2,"em) "):s?f+="translate(calc(-50% + ".concat(t.x/rt,"em), calc(-50% + ").concat(t.y/rt,"em)) "):f+="translate(".concat(t.x/rt,"em, ").concat(t.y/rt,"em) "),f+="scale(".concat(t.size/rt*(t.flipX?-1:1),", ").concat(t.size/rt*(t.flipY?-1:1),") "),f+="rotate(".concat(t.rotate,"deg) "),f}var Dr=`:root, :host {
  --fa-font-solid: normal 900 1em/1 "Font Awesome 6 Solid";
  --fa-font-regular: normal 400 1em/1 "Font Awesome 6 Regular";
  --fa-font-light: normal 300 1em/1 "Font Awesome 6 Light";
  --fa-font-thin: normal 100 1em/1 "Font Awesome 6 Thin";
  --fa-font-duotone: normal 900 1em/1 "Font Awesome 6 Duotone";
  --fa-font-sharp-solid: normal 900 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-regular: normal 400 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-light: normal 300 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-thin: normal 100 1em/1 "Font Awesome 6 Sharp";
  --fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands";
}

svg:not(:root).svg-inline--fa, svg:not(:host).svg-inline--fa {
  overflow: visible;
  box-sizing: content-box;
}

.svg-inline--fa {
  display: var(--fa-display, inline-block);
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-2xs {
  vertical-align: 0.1em;
}
.svg-inline--fa.fa-xs {
  vertical-align: 0em;
}
.svg-inline--fa.fa-sm {
  vertical-align: -0.0714285705em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.2em;
}
.svg-inline--fa.fa-xl {
  vertical-align: -0.25em;
}
.svg-inline--fa.fa-2xl {
  vertical-align: -0.3125em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-li {
  width: var(--fa-li-width, 2em);
  top: 0.25em;
}
.svg-inline--fa.fa-fw {
  width: var(--fa-fw-width, 1.25em);
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  -webkit-transform-origin: center center;
          transform-origin: center center;
}

.fa-layers-counter {
  background-color: var(--fa-counter-background-color, #ff253a);
  border-radius: var(--fa-counter-border-radius, 1em);
  box-sizing: border-box;
  color: var(--fa-inverse, #fff);
  line-height: var(--fa-counter-line-height, 1);
  max-width: var(--fa-counter-max-width, 5em);
  min-width: var(--fa-counter-min-width, 1.5em);
  overflow: hidden;
  padding: var(--fa-counter-padding, 0.25em 0.5em);
  right: var(--fa-right, 0);
  text-overflow: ellipsis;
  top: var(--fa-top, 0);
  -webkit-transform: scale(var(--fa-counter-scale, 0.25));
          transform: scale(var(--fa-counter-scale, 0.25));
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: var(--fa-bottom, 0);
  right: var(--fa-right, 0);
  top: auto;
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: bottom right;
          transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: var(--fa-bottom, 0);
  left: var(--fa-left, 0);
  right: auto;
  top: auto;
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: bottom left;
          transform-origin: bottom left;
}

.fa-layers-top-right {
  top: var(--fa-top, 0);
  right: var(--fa-right, 0);
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: top right;
          transform-origin: top right;
}

.fa-layers-top-left {
  left: var(--fa-left, 0);
  right: auto;
  top: var(--fa-top, 0);
  -webkit-transform: scale(var(--fa-layers-scale, 0.25));
          transform: scale(var(--fa-layers-scale, 0.25));
  -webkit-transform-origin: top left;
          transform-origin: top left;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-2xs {
  font-size: 0.625em;
  line-height: 0.1em;
  vertical-align: 0.225em;
}

.fa-xs {
  font-size: 0.75em;
  line-height: 0.0833333337em;
  vertical-align: 0.125em;
}

.fa-sm {
  font-size: 0.875em;
  line-height: 0.0714285718em;
  vertical-align: 0.0535714295em;
}

.fa-lg {
  font-size: 1.25em;
  line-height: 0.05em;
  vertical-align: -0.075em;
}

.fa-xl {
  font-size: 1.5em;
  line-height: 0.0416666682em;
  vertical-align: -0.125em;
}

.fa-2xl {
  font-size: 2em;
  line-height: 0.03125em;
  vertical-align: -0.1875em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: var(--fa-li-margin, 2.5em);
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: calc(var(--fa-li-width, 2em) * -1);
  position: absolute;
  text-align: center;
  width: var(--fa-li-width, 2em);
  line-height: inherit;
}

.fa-border {
  border-color: var(--fa-border-color, #eee);
  border-radius: var(--fa-border-radius, 0.1em);
  border-style: var(--fa-border-style, solid);
  border-width: var(--fa-border-width, 0.08em);
  padding: var(--fa-border-padding, 0.2em 0.25em 0.15em);
}

.fa-pull-left {
  float: left;
  margin-right: var(--fa-pull-margin, 0.3em);
}

.fa-pull-right {
  float: right;
  margin-left: var(--fa-pull-margin, 0.3em);
}

.fa-beat {
  -webkit-animation-name: fa-beat;
          animation-name: fa-beat;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, ease-in-out);
          animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-bounce {
  -webkit-animation-name: fa-bounce;
          animation-name: fa-bounce;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
}

.fa-fade {
  -webkit-animation-name: fa-fade;
          animation-name: fa-fade;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-beat-fade {
  -webkit-animation-name: fa-beat-fade;
          animation-name: fa-beat-fade;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
          animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-flip {
  -webkit-animation-name: fa-flip;
          animation-name: fa-flip;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, ease-in-out);
          animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-shake {
  -webkit-animation-name: fa-shake;
          animation-name: fa-shake;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, linear);
          animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin {
  -webkit-animation-name: fa-spin;
          animation-name: fa-spin;
  -webkit-animation-delay: var(--fa-animation-delay, 0s);
          animation-delay: var(--fa-animation-delay, 0s);
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 2s);
          animation-duration: var(--fa-animation-duration, 2s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, linear);
          animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin-reverse {
  --fa-animation-direction: reverse;
}

.fa-pulse,
.fa-spin-pulse {
  -webkit-animation-name: fa-spin;
          animation-name: fa-spin;
  -webkit-animation-direction: var(--fa-animation-direction, normal);
          animation-direction: var(--fa-animation-direction, normal);
  -webkit-animation-duration: var(--fa-animation-duration, 1s);
          animation-duration: var(--fa-animation-duration, 1s);
  -webkit-animation-iteration-count: var(--fa-animation-iteration-count, infinite);
          animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  -webkit-animation-timing-function: var(--fa-animation-timing, steps(8));
          animation-timing-function: var(--fa-animation-timing, steps(8));
}

@media (prefers-reduced-motion: reduce) {
  .fa-beat,
.fa-bounce,
.fa-fade,
.fa-beat-fade,
.fa-flip,
.fa-pulse,
.fa-shake,
.fa-spin,
.fa-spin-pulse {
    -webkit-animation-delay: -1ms;
            animation-delay: -1ms;
    -webkit-animation-duration: 1ms;
            animation-duration: 1ms;
    -webkit-animation-iteration-count: 1;
            animation-iteration-count: 1;
    -webkit-transition-delay: 0s;
            transition-delay: 0s;
    -webkit-transition-duration: 0s;
            transition-duration: 0s;
  }
}
@-webkit-keyframes fa-beat {
  0%, 90% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  45% {
    -webkit-transform: scale(var(--fa-beat-scale, 1.25));
            transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@keyframes fa-beat {
  0%, 90% {
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  45% {
    -webkit-transform: scale(var(--fa-beat-scale, 1.25));
            transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@-webkit-keyframes fa-bounce {
  0% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  10% {
    -webkit-transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
            transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    -webkit-transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
            transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    -webkit-transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
            transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    -webkit-transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
            transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  100% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
}
@keyframes fa-bounce {
  0% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  10% {
    -webkit-transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
            transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    -webkit-transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
            transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    -webkit-transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
            transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    -webkit-transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
            transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
  100% {
    -webkit-transform: scale(1, 1) translateY(0);
            transform: scale(1, 1) translateY(0);
  }
}
@-webkit-keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@-webkit-keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  50% {
    opacity: 1;
    -webkit-transform: scale(var(--fa-beat-fade-scale, 1.125));
            transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    -webkit-transform: scale(1);
            transform: scale(1);
  }
  50% {
    opacity: 1;
    -webkit-transform: scale(var(--fa-beat-fade-scale, 1.125));
            transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@-webkit-keyframes fa-flip {
  50% {
    -webkit-transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
            transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@keyframes fa-flip {
  50% {
    -webkit-transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
            transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@-webkit-keyframes fa-shake {
  0% {
    -webkit-transform: rotate(-15deg);
            transform: rotate(-15deg);
  }
  4% {
    -webkit-transform: rotate(15deg);
            transform: rotate(15deg);
  }
  8%, 24% {
    -webkit-transform: rotate(-18deg);
            transform: rotate(-18deg);
  }
  12%, 28% {
    -webkit-transform: rotate(18deg);
            transform: rotate(18deg);
  }
  16% {
    -webkit-transform: rotate(-22deg);
            transform: rotate(-22deg);
  }
  20% {
    -webkit-transform: rotate(22deg);
            transform: rotate(22deg);
  }
  32% {
    -webkit-transform: rotate(-12deg);
            transform: rotate(-12deg);
  }
  36% {
    -webkit-transform: rotate(12deg);
            transform: rotate(12deg);
  }
  40%, 100% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
}
@keyframes fa-shake {
  0% {
    -webkit-transform: rotate(-15deg);
            transform: rotate(-15deg);
  }
  4% {
    -webkit-transform: rotate(15deg);
            transform: rotate(15deg);
  }
  8%, 24% {
    -webkit-transform: rotate(-18deg);
            transform: rotate(-18deg);
  }
  12%, 28% {
    -webkit-transform: rotate(18deg);
            transform: rotate(18deg);
  }
  16% {
    -webkit-transform: rotate(-22deg);
            transform: rotate(-22deg);
  }
  20% {
    -webkit-transform: rotate(22deg);
            transform: rotate(22deg);
  }
  32% {
    -webkit-transform: rotate(-12deg);
            transform: rotate(-12deg);
  }
  36% {
    -webkit-transform: rotate(12deg);
            transform: rotate(12deg);
  }
  40%, 100% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg);
}

.fa-rotate-180 {
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg);
}

.fa-rotate-270 {
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg);
}

.fa-flip-horizontal {
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1);
}

.fa-flip-vertical {
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1);
}

.fa-flip-both,
.fa-flip-horizontal.fa-flip-vertical {
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1);
}

.fa-rotate-by {
  -webkit-transform: rotate(var(--fa-rotate-angle, 0));
          transform: rotate(var(--fa-rotate-angle, 0));
}

.fa-stack {
  display: inline-block;
  vertical-align: middle;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
  z-index: var(--fa-stack-z-index, auto);
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: var(--fa-inverse, #fff);
}

.sr-only,
.fa-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only-focusable:not(:focus),
.fa-sr-only-focusable:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}

.fad.fa-inverse,
.fa-duotone.fa-inverse {
  color: var(--fa-inverse, #fff);
}`;function Vn(){var e=Rn,t=Fn,n=g.cssPrefix,a=g.replacementClass,r=Dr;if(n!==e||a!==t){var o=new RegExp("\\.".concat(e,"\\-"),"g"),i=new RegExp("\\--".concat(e,"\\-"),"g"),s=new RegExp("\\.".concat(t),"g");r=r.replace(o,".".concat(n,"-")).replace(i,"--".concat(n,"-")).replace(s,".".concat(a))}return r}var Bn=!1;function Le(){g.autoAddCss&&!Bn&&(jr(Vn()),Bn=!0)}var Yr={mixout:function(){return{dom:{css:Vn,insertCss:Le}}},hooks:function(){return{beforeDOMElementCreation:function(){Le()},beforeI2svg:function(){Le()}}}},Q=at||{};Q[J]||(Q[J]={}),Q[J].styles||(Q[J].styles={}),Q[J].hooks||(Q[J].hooks={}),Q[J].shims||(Q[J].shims=[]);var B=Q[J],Gn=[],Hr=function e(){x.removeEventListener("DOMContentLoaded",e),ee=1,Gn.map(function(t){return t()})},ee=!1;K&&(ee=(x.documentElement.doScroll?/^loaded|^c/:/^loaded|^i|^c/).test(x.readyState),ee||x.addEventListener("DOMContentLoaded",Hr));function Ur(e){K&&(ee?setTimeout(e,0):Gn.push(e))}function zt(e){var t=e.tag,n=e.attributes,a=n===void 0?{}:n,r=e.children,o=r===void 0?[]:r;return typeof e=="string"?Wn(e):"<".concat(t," ").concat(Rr(a),">").concat(o.map(zt).join(""),"</").concat(t,">")}function Xn(e,t,n){if(e&&e[t]&&e[t][n])return{prefix:t,iconName:n,icon:e[t][n]}}var Wr=function(t,n){return function(a,r,o,i){return t.call(n,a,r,o,i)}},Re=function(t,n,a,r){var o=Object.keys(t),i=o.length,s=r!==void 0?Wr(n,r):n,f,l,u;for(a===void 0?(f=1,u=t[o[0]]):(f=0,u=a);f<i;f++)l=o[f],u=s(u,t[l],l,t);return u};function Vr(e){for(var t=[],n=0,a=e.length;n<a;){var r=e.charCodeAt(n++);if(r>=55296&&r<=56319&&n<a){var o=e.charCodeAt(n++);(o&64512)==56320?t.push(((r&1023)<<10)+(o&1023)+65536):(t.push(r),n--)}else t.push(r)}return t}function Fe(e){var t=Vr(e);return t.length===1?t[0].toString(16):null}function Br(e,t){var n=e.length,a=e.charCodeAt(t),r;return a>=55296&&a<=56319&&n>t+1&&(r=e.charCodeAt(t+1),r>=56320&&r<=57343)?(a-55296)*1024+r-56320+65536:a}function qn(e){return Object.keys(e).reduce(function(t,n){var a=e[n],r=!!a.icon;return r?t[a.iconName]=a.icon:t[n]=a,t},{})}function ze(e,t){var n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{},a=n.skipHooks,r=a===void 0?!1:a,o=qn(t);typeof B.hooks.addPack=="function"&&!r?B.hooks.addPack(e,qn(t)):B.styles[e]=d(d({},B.styles[e]||{}),o),e==="fas"&&ze("fa",t)}var ne,ae,re,kt=B.styles,Gr=B.shims,Xr=(ne={},I(ne,A,Object.values(Mt[A])),I(ne,O,Object.values(Mt[O])),ne),De=null,Kn={},Jn={},Qn={},Zn={},$n={},qr=(ae={},I(ae,A,Object.keys(It[A])),I(ae,O,Object.keys(It[O])),ae);function Kr(e){return~Nr.indexOf(e)}function Jr(e,t){var n=t.split("-"),a=n[0],r=n.slice(1).join("-");return a===e&&r!==""&&!Kr(r)?r:null}var ta=function(){var t=function(o){return Re(kt,function(i,s,f){return i[f]=Re(s,o,{}),i},{})};Kn=t(function(r,o,i){if(o[3]&&(r[o[3]]=i),o[2]){var s=o[2].filter(function(f){return typeof f=="number"});s.forEach(function(f){r[f.toString(16)]=i})}return r}),Jn=t(function(r,o,i){if(r[i]=i,o[2]){var s=o[2].filter(function(f){return typeof f=="string"});s.forEach(function(f){r[f]=i})}return r}),$n=t(function(r,o,i){var s=o[2];return r[i]=i,s.forEach(function(f){r[f]=i}),r});var n="far"in kt||g.autoFetchSvg,a=Re(Gr,function(r,o){var i=o[0],s=o[1],f=o[2];return s==="far"&&!n&&(s="fas"),typeof i=="string"&&(r.names[i]={prefix:s,iconName:f}),typeof i=="number"&&(r.unicodes[i.toString(16)]={prefix:s,iconName:f}),r},{names:{},unicodes:{}});Qn=a.names,Zn=a.unicodes,De=ie(g.styleDefault,{family:g.familyDefault})};Mr(function(e){De=ie(e.styleDefault,{family:g.familyDefault})}),ta();function Ye(e,t){return(Kn[e]||{})[t]}function Qr(e,t){return(Jn[e]||{})[t]}function ut(e,t){return($n[e]||{})[t]}function ea(e){return Qn[e]||{prefix:null,iconName:null}}function Zr(e){var t=Zn[e],n=Ye("fas",e);return t||(n?{prefix:"fas",iconName:n}:null)||{prefix:null,iconName:null}}function it(){return De}var He=function(){return{prefix:null,iconName:null,rest:[]}};function ie(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},n=t.family,a=n===void 0?A:n,r=It[a][e],o=Tt[a][e]||Tt[a][r],i=e in B.styles?e:null;return o||i||null}var na=(re={},I(re,A,Object.keys(Mt[A])),I(re,O,Object.keys(Mt[O])),re);function oe(e){var t,n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},a=n.skipLookups,r=a===void 0?!1:a,o=(t={},I(t,A,"".concat(g.cssPrefix,"-").concat(A)),I(t,O,"".concat(g.cssPrefix,"-").concat(O)),t),i=null,s=A;(e.includes(o[A])||e.some(function(l){return na[A].includes(l)}))&&(s=A),(e.includes(o[O])||e.some(function(l){return na[O].includes(l)}))&&(s=O);var f=e.reduce(function(l,u){var c=Jr(g.cssPrefix,u);if(kt[u]?(u=Xr[s].includes(u)?xr[s][u]:u,i=u,l.prefix=u):qr[s].indexOf(u)>-1?(i=u,l.prefix=ie(u,{family:s})):c?l.iconName=c:u!==g.replacementClass&&u!==o[A]&&u!==o[O]&&l.rest.push(u),!r&&l.prefix&&l.iconName){var p=i==="fa"?ea(l.iconName):{},h=ut(l.prefix,l.iconName);p.prefix&&(i=null),l.iconName=p.iconName||h||l.iconName,l.prefix=p.prefix||l.prefix,l.prefix==="far"&&!kt.far&&kt.fas&&!g.autoFetchSvg&&(l.prefix="fas")}return l},He());return(e.includes("fa-brands")||e.includes("fab"))&&(f.prefix="fab"),(e.includes("fa-duotone")||e.includes("fad"))&&(f.prefix="fad"),!f.prefix&&s===O&&(kt.fass||g.autoFetchSvg)&&(f.prefix="fass",f.iconName=ut(f.prefix,f.iconName)||f.iconName),(f.prefix==="fa"||i==="fa")&&(f.prefix=it()||"fas"),f}var $r=function(){function e(){ur(this,e),this.definitions={}}return mr(e,[{key:"add",value:function(){for(var n=this,a=arguments.length,r=new Array(a),o=0;o<a;o++)r[o]=arguments[o];var i=r.reduce(this._pullDefinitions,{});Object.keys(i).forEach(function(s){n.definitions[s]=d(d({},n.definitions[s]||{}),i[s]),ze(s,i[s]);var f=Mt[A][s];f&&ze(f,i[s]),ta()})}},{key:"reset",value:function(){this.definitions={}}},{key:"_pullDefinitions",value:function(n,a){var r=a.prefix&&a.iconName&&a.icon?{0:a}:a;return Object.keys(r).map(function(o){var i=r[o],s=i.prefix,f=i.iconName,l=i.icon,u=l[2];n[s]||(n[s]={}),u.length>0&&u.forEach(function(c){typeof c=="string"&&(n[s][c]=l)}),n[s][f]=l}),n}}]),e}(),aa=[],wt={},xt={},ti=Object.keys(xt);function ei(e,t){var n=t.mixoutsTo;return aa=e,wt={},Object.keys(xt).forEach(function(a){ti.indexOf(a)===-1&&delete xt[a]}),aa.forEach(function(a){var r=a.mixout?a.mixout():{};if(Object.keys(r).forEach(function(i){typeof r[i]=="function"&&(n[i]=r[i]),Xt(r[i])==="object"&&Object.keys(r[i]).forEach(function(s){n[i]||(n[i]={}),n[i][s]=r[i][s]})}),a.hooks){var o=a.hooks();Object.keys(o).forEach(function(i){wt[i]||(wt[i]=[]),wt[i].push(o[i])})}a.provides&&a.provides(xt)}),n}function Ue(e,t){for(var n=arguments.length,a=new Array(n>2?n-2:0),r=2;r<n;r++)a[r-2]=arguments[r];var o=wt[e]||[];return o.forEach(function(i){t=i.apply(null,[t].concat(a))}),t}function mt(e){for(var t=arguments.length,n=new Array(t>1?t-1:0),a=1;a<t;a++)n[a-1]=arguments[a];var r=wt[e]||[];r.forEach(function(o){o.apply(null,n)})}function Z(){var e=arguments[0],t=Array.prototype.slice.call(arguments,1);return xt[e]?xt[e].apply(null,t):void 0}function We(e){e.prefix==="fa"&&(e.prefix="fas");var t=e.iconName,n=e.prefix||it();if(t)return t=ut(n,t)||t,Xn(ra.definitions,n,t)||Xn(B.styles,n,t)}var ra=new $r,ni=function(){g.autoReplaceSvg=!1,g.observeMutations=!1,mt("noAuto")},ai={i2svg:function(){var t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};return K?(mt("beforeI2svg",t),Z("pseudoElements2svg",t),Z("i2svg",t)):Promise.reject("Operation requires a DOM of some kind.")},watch:function(){var t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{},n=t.autoReplaceSvgRoot;g.autoReplaceSvg===!1&&(g.autoReplaceSvg=!0),g.observeMutations=!0,Ur(function(){ii({autoReplaceSvgRoot:n}),mt("watch",t)})}},ri={icon:function(t){if(t===null)return null;if(Xt(t)==="object"&&t.prefix&&t.iconName)return{prefix:t.prefix,iconName:ut(t.prefix,t.iconName)||t.iconName};if(Array.isArray(t)&&t.length===2){var n=t[1].indexOf("fa-")===0?t[1].slice(3):t[1],a=ie(t[0]);return{prefix:a,iconName:ut(a,n)||n}}if(typeof t=="string"&&(t.indexOf("".concat(g.cssPrefix,"-"))>-1||t.match(Ar))){var r=oe(t.split(" "),{skipLookups:!0});return{prefix:r.prefix||it(),iconName:ut(r.prefix,r.iconName)||r.iconName}}if(typeof t=="string"){var o=it();return{prefix:o,iconName:ut(o,t)||t}}}},Y={noAuto:ni,config:g,dom:ai,parse:ri,library:ra,findIconDefinition:We,toHtml:zt},ii=function(){var t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{},n=t.autoReplaceSvgRoot,a=n===void 0?x:n;(Object.keys(B.styles).length>0||g.autoFetchSvg)&&K&&g.autoReplaceSvg&&Y.dom.i2svg({node:a})};function se(e,t){return Object.defineProperty(e,"abstract",{get:t}),Object.defineProperty(e,"html",{get:function(){return e.abstract.map(function(a){return zt(a)})}}),Object.defineProperty(e,"node",{get:function(){if(K){var a=x.createElement("div");return a.innerHTML=e.html,a.children}}}),e}function oi(e){var t=e.children,n=e.main,a=e.mask,r=e.attributes,o=e.styles,i=e.transform;if(je(i)&&n.found&&!a.found){var s=n.width,f=n.height,l={x:s/f/2,y:.5};r.style=te(d(d({},o),{},{"transform-origin":"".concat(l.x+i.x/16,"em ").concat(l.y+i.y/16,"em")}))}return[{tag:"svg",attributes:r,children:t}]}function si(e){var t=e.prefix,n=e.iconName,a=e.children,r=e.attributes,o=e.symbol,i=o===!0?"".concat(t,"-").concat(g.cssPrefix,"-").concat(n):o;return[{tag:"svg",attributes:{style:"display: none;"},children:[{tag:"symbol",attributes:d(d({},r),{},{id:i}),children:a}]}]}function Ve(e){var t=e.icons,n=t.main,a=t.mask,r=e.prefix,o=e.iconName,i=e.transform,s=e.symbol,f=e.title,l=e.maskId,u=e.titleId,c=e.extra,p=e.watchable,h=p===void 0?!1:p,m=a.found?a:n,y=m.width,b=m.height,S=r==="fak",w=[g.replacementClass,o?"".concat(g.cssPrefix,"-").concat(o):""].filter(function(H){return c.classes.indexOf(H)===-1}).filter(function(H){return H!==""||!!H}).concat(c.classes).join(" "),N={children:[],attributes:d(d({},c.attributes),{},{"data-prefix":r,"data-icon":o,class:w,role:c.attributes.role||"img",xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 ".concat(y," ").concat(b)})},T=S&&!~c.classes.indexOf("fa-fw")?{width:"".concat(y/b*16*.0625,"em")}:{};h&&(N.attributes[lt]=""),f&&(N.children.push({tag:"title",attributes:{id:N.attributes["aria-labelledby"]||"title-".concat(u||Ft())},children:[f]}),delete N.attributes.title);var M=d(d({},N),{},{prefix:r,iconName:o,main:n,mask:a,maskId:l,transform:i,symbol:s,styles:d(d({},T),c.styles)}),X=a.found&&n.found?Z("generateAbstractMask",M)||{children:[],attributes:{}}:Z("generateAbstractIcon",M)||{children:[],attributes:{}},q=X.children,At=X.attributes;return M.children=q,M.attributes=At,s?si(M):oi(M)}function ia(e){var t=e.content,n=e.width,a=e.height,r=e.transform,o=e.title,i=e.extra,s=e.watchable,f=s===void 0?!1:s,l=d(d(d({},i.attributes),o?{title:o}:{}),{},{class:i.classes.join(" ")});f&&(l[lt]="");var u=d({},i.styles);je(r)&&(u.transform=zr({transform:r,startCentered:!0,width:n,height:a}),u["-webkit-transform"]=u.transform);var c=te(u);c.length>0&&(l.style=c);var p=[];return p.push({tag:"span",attributes:l,children:[t]}),o&&p.push({tag:"span",attributes:{class:"sr-only"},children:[o]}),p}function fi(e){var t=e.content,n=e.title,a=e.extra,r=d(d(d({},a.attributes),n?{title:n}:{}),{},{class:a.classes.join(" ")}),o=te(a.styles);o.length>0&&(r.style=o);var i=[];return i.push({tag:"span",attributes:r,children:[t]}),n&&i.push({tag:"span",attributes:{class:"sr-only"},children:[n]}),i}var Be=B.styles;function Ge(e){var t=e[0],n=e[1],a=e.slice(4),r=Ee(a,1),o=r[0],i=null;return Array.isArray(o)?i={tag:"g",attributes:{class:"".concat(g.cssPrefix,"-").concat(ct.GROUP)},children:[{tag:"path",attributes:{class:"".concat(g.cssPrefix,"-").concat(ct.SECONDARY),fill:"currentColor",d:o[0]}},{tag:"path",attributes:{class:"".concat(g.cssPrefix,"-").concat(ct.PRIMARY),fill:"currentColor",d:o[1]}}]}:i={tag:"path",attributes:{fill:"currentColor",d:o}},{found:!0,width:t,height:n,icon:i}}var li={found:!1,width:512,height:512};function ci(e,t){!Dn&&!g.showMissingIcons&&e&&console.error('Icon with name "'.concat(e,'" and prefix "').concat(t,'" is missing.'))}function Xe(e,t){var n=t;return t==="fa"&&g.styleDefault!==null&&(t=it()),new Promise(function(a,r){if(Z("missingIconAbstract"),n==="fa"){var o=ea(e)||{};e=o.iconName||e,t=o.prefix||t}if(e&&t&&Be[t]&&Be[t][e]){var i=Be[t][e];return a(Ge(i))}ci(e,t),a(d(d({},li),{},{icon:g.showMissingIcons&&e?Z("missingIconAbstract")||{}:{}}))})}var oa=function(){},qe=g.measurePerformance&&qt&&qt.mark&&qt.measure?qt:{mark:oa,measure:oa},Dt='FA "6.5.2"',ui=function(t){return qe.mark("".concat(Dt," ").concat(t," begins")),function(){return sa(t)}},sa=function(t){qe.mark("".concat(Dt," ").concat(t," ends")),qe.measure("".concat(Dt," ").concat(t),"".concat(Dt," ").concat(t," begins"),"".concat(Dt," ").concat(t," ends"))},Ke={begin:ui,end:sa},fe=function(){};function fa(e){var t=e.getAttribute?e.getAttribute(lt):null;return typeof t=="string"}function mi(e){var t=e.getAttribute?e.getAttribute(Pe):null,n=e.getAttribute?e.getAttribute(Ie):null;return t&&n}function di(e){return e&&e.classList&&e.classList.contains&&e.classList.contains(g.replacementClass)}function gi(){if(g.autoReplaceSvg===!0)return le.replace;var e=le[g.autoReplaceSvg];return e||le.replace}function vi(e){return x.createElementNS("http://www.w3.org/2000/svg",e)}function pi(e){return x.createElement(e)}function la(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},n=t.ceFn,a=n===void 0?e.tag==="svg"?vi:pi:n;if(typeof e=="string")return x.createTextNode(e);var r=a(e.tag);Object.keys(e.attributes||[]).forEach(function(i){r.setAttribute(i,e.attributes[i])});var o=e.children||[];return o.forEach(function(i){r.appendChild(la(i,{ceFn:a}))}),r}function bi(e){var t=" ".concat(e.outerHTML," ");return t="".concat(t,"Font Awesome fontawesome.com "),t}var le={replace:function(t){var n=t[0];if(n.parentNode)if(t[1].forEach(function(r){n.parentNode.insertBefore(la(r),n)}),n.getAttribute(lt)===null&&g.keepOriginalSource){var a=x.createComment(bi(n));n.parentNode.replaceChild(a,n)}else n.remove()},nest:function(t){var n=t[0],a=t[1];if(~Me(n).indexOf(g.replacementClass))return le.replace(t);var r=new RegExp("".concat(g.cssPrefix,"-.*"));if(delete a[0].attributes.id,a[0].attributes.class){var o=a[0].attributes.class.split(" ").reduce(function(s,f){return f===g.replacementClass||f.match(r)?s.toSvg.push(f):s.toNode.push(f),s},{toNode:[],toSvg:[]});a[0].attributes.class=o.toSvg.join(" "),o.toNode.length===0?n.removeAttribute("class"):n.setAttribute("class",o.toNode.join(" "))}var i=a.map(function(s){return zt(s)}).join(`
`);n.setAttribute(lt,""),n.innerHTML=i}};function ca(e){e()}function ua(e,t){var n=typeof t=="function"?t:fe;if(e.length===0)n();else{var a=ca;g.mutateApproach===kr&&(a=at.requestAnimationFrame||ca),a(function(){var r=gi(),o=Ke.begin("mutate");e.map(r),o(),n()})}}var Je=!1;function ma(){Je=!0}function Qe(){Je=!1}var ce=null;function da(e){if(jn&&g.observeMutations){var t=e.treeCallback,n=t===void 0?fe:t,a=e.nodeCallback,r=a===void 0?fe:a,o=e.pseudoElementsCallback,i=o===void 0?fe:o,s=e.observeMutationsRoot,f=s===void 0?x:s;ce=new jn(function(l){if(!Je){var u=it();_t(l).forEach(function(c){if(c.type==="childList"&&c.addedNodes.length>0&&!fa(c.addedNodes[0])&&(g.searchPseudoElements&&i(c.target),n(c.target)),c.type==="attributes"&&c.target.parentNode&&g.searchPseudoElements&&i(c.target.parentNode),c.type==="attributes"&&fa(c.target)&&~Cr.indexOf(c.attributeName))if(c.attributeName==="class"&&mi(c.target)){var p=oe(Me(c.target)),h=p.prefix,m=p.iconName;c.target.setAttribute(Pe,h||u),m&&c.target.setAttribute(Ie,m)}else di(c.target)&&r(c.target)})}}),K&&ce.observe(f,{childList:!0,attributes:!0,characterData:!0,subtree:!0})}}function hi(){ce&&ce.disconnect()}function yi(e){var t=e.getAttribute("style"),n=[];return t&&(n=t.split(";").reduce(function(a,r){var o=r.split(":"),i=o[0],s=o.slice(1);return i&&s.length>0&&(a[i]=s.join(":").trim()),a},{})),n}function _i(e){var t=e.getAttribute("data-prefix"),n=e.getAttribute("data-icon"),a=e.innerText!==void 0?e.innerText.trim():"",r=oe(Me(e));return r.prefix||(r.prefix=it()),t&&n&&(r.prefix=t,r.iconName=n),r.iconName&&r.prefix||(r.prefix&&a.length>0&&(r.iconName=Qr(r.prefix,e.innerText)||Ye(r.prefix,Fe(e.innerText))),!r.iconName&&g.autoFetchSvg&&e.firstChild&&e.firstChild.nodeType===Node.TEXT_NODE&&(r.iconName=e.firstChild.data)),r}function ki(e){var t=_t(e.attributes).reduce(function(r,o){return r.name!=="class"&&r.name!=="style"&&(r[o.name]=o.value),r},{}),n=e.getAttribute("title"),a=e.getAttribute("data-fa-title-id");return g.autoA11y&&(n?t["aria-labelledby"]="".concat(g.replacementClass,"-title-").concat(a||Ft()):(t["aria-hidden"]="true",t.focusable="false")),t}function wi(){return{iconName:null,title:null,titleId:null,prefix:null,transform:G,symbol:!1,mask:{iconName:null,prefix:null,rest:[]},maskId:null,extra:{classes:[],styles:{},attributes:{}}}}function ga(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{styleParser:!0},n=_i(e),a=n.iconName,r=n.prefix,o=n.rest,i=ki(e),s=Ue("parseNodeAttributes",{},e),f=t.styleParser?yi(e):[];return d({iconName:a,title:e.getAttribute("title"),titleId:e.getAttribute("data-fa-title-id"),prefix:r,transform:G,mask:{iconName:null,prefix:null,rest:[]},maskId:null,symbol:!1,extra:{classes:o,styles:f,attributes:i}},s)}var xi=B.styles;function va(e){var t=g.autoReplaceSvg==="nest"?ga(e,{styleParser:!1}):ga(e);return~t.extra.classes.indexOf(Yn)?Z("generateLayersText",e,t):Z("generateSvgReplacementMutation",e,t)}var ot=new Set;Te.map(function(e){ot.add("fa-".concat(e))}),Object.keys(It[A]).map(ot.add.bind(ot)),Object.keys(It[O]).map(ot.add.bind(ot)),ot=Nt(ot);function pa(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:null;if(!K)return Promise.resolve();var n=x.documentElement.classList,a=function(c){return n.add("".concat(zn,"-").concat(c))},r=function(c){return n.remove("".concat(zn,"-").concat(c))},o=g.autoFetchSvg?ot:Te.map(function(u){return"fa-".concat(u)}).concat(Object.keys(xi));o.includes("fa")||o.push("fa");var i=[".".concat(Yn,":not([").concat(lt,"])")].concat(o.map(function(u){return".".concat(u,":not([").concat(lt,"])")})).join(", ");if(i.length===0)return Promise.resolve();var s=[];try{s=_t(e.querySelectorAll(i))}catch{}if(s.length>0)a("pending"),r("complete");else return Promise.resolve();var f=Ke.begin("onTree"),l=s.reduce(function(u,c){try{var p=va(c);p&&u.push(p)}catch(h){Dn||h.name==="MissingIcon"&&console.error(h)}return u},[]);return new Promise(function(u,c){Promise.all(l).then(function(p){ua(p,function(){a("active"),a("complete"),r("pending"),typeof t=="function"&&t(),f(),u()})}).catch(function(p){f(),c(p)})})}function Ai(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:null;va(e).then(function(n){n&&ua([n],t)})}function Ei(e){return function(t){var n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},a=(t||{}).icon?t:We(t||{}),r=n.mask;return r&&(r=(r||{}).icon?r:We(r||{})),e(a,d(d({},n),{},{mask:r}))}}var Si=function(t){var n=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},a=n.transform,r=a===void 0?G:a,o=n.symbol,i=o===void 0?!1:o,s=n.mask,f=s===void 0?null:s,l=n.maskId,u=l===void 0?null:l,c=n.title,p=c===void 0?null:c,h=n.titleId,m=h===void 0?null:h,y=n.classes,b=y===void 0?[]:y,S=n.attributes,w=S===void 0?{}:S,N=n.styles,T=N===void 0?{}:N;if(t){var M=t.prefix,X=t.iconName,q=t.icon;return se(d({type:"icon"},t),function(){return mt("beforeDOMElementCreation",{iconDefinition:t,params:n}),g.autoA11y&&(p?w["aria-labelledby"]="".concat(g.replacementClass,"-title-").concat(m||Ft()):(w["aria-hidden"]="true",w.focusable="false")),Ve({icons:{main:Ge(q),mask:f?Ge(f.icon):{found:!1,width:null,height:null,icon:{}}},prefix:M,iconName:X,transform:d(d({},G),r),symbol:i,title:p,maskId:u,titleId:m,extra:{attributes:w,styles:T,classes:b}})})}},Oi={mixout:function(){return{icon:Ei(Si)}},hooks:function(){return{mutationObserverCallbacks:function(n){return n.treeCallback=pa,n.nodeCallback=Ai,n}}},provides:function(t){t.i2svg=function(n){var a=n.node,r=a===void 0?x:a,o=n.callback,i=o===void 0?function(){}:o;return pa(r,i)},t.generateSvgReplacementMutation=function(n,a){var r=a.iconName,o=a.title,i=a.titleId,s=a.prefix,f=a.transform,l=a.symbol,u=a.mask,c=a.maskId,p=a.extra;return new Promise(function(h,m){Promise.all([Xe(r,s),u.iconName?Xe(u.iconName,u.prefix):Promise.resolve({found:!1,width:512,height:512,icon:{}})]).then(function(y){var b=Ee(y,2),S=b[0],w=b[1];h([n,Ve({icons:{main:S,mask:w},prefix:s,iconName:r,transform:f,symbol:l,maskId:c,title:o,titleId:i,extra:p,watchable:!0})])}).catch(m)})},t.generateAbstractIcon=function(n){var a=n.children,r=n.attributes,o=n.main,i=n.transform,s=n.styles,f=te(s);f.length>0&&(r.style=f);var l;return je(i)&&(l=Z("generateAbstractTransformGrouping",{main:o,transform:i,containerWidth:o.width,iconWidth:o.width})),a.push(l||o.icon),{children:a,attributes:r}}}},Ci={mixout:function(){return{layer:function(n){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},r=a.classes,o=r===void 0?[]:r;return se({type:"layer"},function(){mt("beforeDOMElementCreation",{assembler:n,params:a});var i=[];return n(function(s){Array.isArray(s)?s.map(function(f){i=i.concat(f.abstract)}):i=i.concat(s.abstract)}),[{tag:"span",attributes:{class:["".concat(g.cssPrefix,"-layers")].concat(Nt(o)).join(" ")},children:i}]})}}}},Ni={mixout:function(){return{counter:function(n){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},r=a.title,o=r===void 0?null:r,i=a.classes,s=i===void 0?[]:i,f=a.attributes,l=f===void 0?{}:f,u=a.styles,c=u===void 0?{}:u;return se({type:"counter",content:n},function(){return mt("beforeDOMElementCreation",{content:n,params:a}),fi({content:n.toString(),title:o,extra:{attributes:l,styles:c,classes:["".concat(g.cssPrefix,"-layers-counter")].concat(Nt(s))}})})}}}},Pi={mixout:function(){return{text:function(n){var a=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},r=a.transform,o=r===void 0?G:r,i=a.title,s=i===void 0?null:i,f=a.classes,l=f===void 0?[]:f,u=a.attributes,c=u===void 0?{}:u,p=a.styles,h=p===void 0?{}:p;return se({type:"text",content:n},function(){return mt("beforeDOMElementCreation",{content:n,params:a}),ia({content:n,transform:d(d({},G),o),title:s,extra:{attributes:c,styles:h,classes:["".concat(g.cssPrefix,"-layers-text")].concat(Nt(l))}})})}}},provides:function(t){t.generateLayersText=function(n,a){var r=a.title,o=a.transform,i=a.extra,s=null,f=null;if(Ln){var l=parseInt(getComputedStyle(n).fontSize,10),u=n.getBoundingClientRect();s=u.width/l,f=u.height/l}return g.autoA11y&&!r&&(i.attributes["aria-hidden"]="true"),Promise.resolve([n,ia({content:n.innerHTML,width:s,height:f,transform:o,title:r,extra:i,watchable:!0})])}}},Ii=new RegExp('"',"ug"),ba=[1105920,1112319];function Ti(e){var t=e.replace(Ii,""),n=Br(t,0),a=n>=ba[0]&&n<=ba[1],r=t.length===2?t[0]===t[1]:!1;return{value:Fe(r?t[0]:t),isSecondary:a||r}}function ha(e,t){var n="".concat(_r).concat(t.replace(":","-"));return new Promise(function(a,r){if(e.getAttribute(n)!==null)return a();var o=_t(e.children),i=o.filter(function(q){return q.getAttribute(Ne)===t})[0],s=at.getComputedStyle(e,t),f=s.getPropertyValue("font-family").match(Er),l=s.getPropertyValue("font-weight"),u=s.getPropertyValue("content");if(i&&!f)return e.removeChild(i),a();if(f&&u!=="none"&&u!==""){var c=s.getPropertyValue("content"),p=~["Sharp"].indexOf(f[2])?O:A,h=~["Solid","Regular","Light","Thin","Duotone","Brands","Kit"].indexOf(f[2])?Tt[p][f[2].toLowerCase()]:Sr[p][l],m=Ti(c),y=m.value,b=m.isSecondary,S=f[0].startsWith("FontAwesome"),w=Ye(h,y),N=w;if(S){var T=Zr(y);T.iconName&&T.prefix&&(w=T.iconName,h=T.prefix)}if(w&&!b&&(!i||i.getAttribute(Pe)!==h||i.getAttribute(Ie)!==N)){e.setAttribute(n,N),i&&e.removeChild(i);var M=wi(),X=M.extra;X.attributes[Ne]=t,Xe(w,h).then(function(q){var At=Ve(d(d({},M),{},{icons:{main:q,mask:He()},prefix:h,iconName:N,extra:X,watchable:!0})),H=x.createElementNS("http://www.w3.org/2000/svg","svg");t==="::before"?e.insertBefore(H,e.firstChild):e.appendChild(H),H.outerHTML=At.map(function(Yt){return zt(Yt)}).join(`
`),e.removeAttribute(n),a()}).catch(r)}else a()}else a()})}function Mi(e){return Promise.all([ha(e,"::before"),ha(e,"::after")])}function ji(e){return e.parentNode!==document.head&&!~wr.indexOf(e.tagName.toUpperCase())&&!e.getAttribute(Ne)&&(!e.parentNode||e.parentNode.tagName!=="svg")}function ya(e){if(K)return new Promise(function(t,n){var a=_t(e.querySelectorAll("*")).filter(ji).map(Mi),r=Ke.begin("searchPseudoElements");ma(),Promise.all(a).then(function(){r(),Qe(),t()}).catch(function(){r(),Qe(),n()})})}var Li={hooks:function(){return{mutationObserverCallbacks:function(n){return n.pseudoElementsCallback=ya,n}}},provides:function(t){t.pseudoElements2svg=function(n){var a=n.node,r=a===void 0?x:a;g.searchPseudoElements&&ya(r)}}},_a=!1,Ri={mixout:function(){return{dom:{unwatch:function(){ma(),_a=!0}}}},hooks:function(){return{bootstrap:function(){da(Ue("mutationObserverCallbacks",{}))},noAuto:function(){hi()},watch:function(n){var a=n.observeMutationsRoot;_a?Qe():da(Ue("mutationObserverCallbacks",{observeMutationsRoot:a}))}}}},ka=function(t){var n={size:16,x:0,y:0,flipX:!1,flipY:!1,rotate:0};return t.toLowerCase().split(" ").reduce(function(a,r){var o=r.toLowerCase().split("-"),i=o[0],s=o.slice(1).join("-");if(i&&s==="h")return a.flipX=!0,a;if(i&&s==="v")return a.flipY=!0,a;if(s=parseFloat(s),isNaN(s))return a;switch(i){case"grow":a.size=a.size+s;break;case"shrink":a.size=a.size-s;break;case"left":a.x=a.x-s;break;case"right":a.x=a.x+s;break;case"up":a.y=a.y-s;break;case"down":a.y=a.y+s;break;case"rotate":a.rotate=a.rotate+s;break}return a},n)},Fi={mixout:function(){return{parse:{transform:function(n){return ka(n)}}}},hooks:function(){return{parseNodeAttributes:function(n,a){var r=a.getAttribute("data-fa-transform");return r&&(n.transform=ka(r)),n}}},provides:function(t){t.generateAbstractTransformGrouping=function(n){var a=n.main,r=n.transform,o=n.containerWidth,i=n.iconWidth,s={transform:"translate(".concat(o/2," 256)")},f="translate(".concat(r.x*32,", ").concat(r.y*32,") "),l="scale(".concat(r.size/16*(r.flipX?-1:1),", ").concat(r.size/16*(r.flipY?-1:1),") "),u="rotate(".concat(r.rotate," 0 0)"),c={transform:"".concat(f," ").concat(l," ").concat(u)},p={transform:"translate(".concat(i/2*-1," -256)")},h={outer:s,inner:c,path:p};return{tag:"g",attributes:d({},h.outer),children:[{tag:"g",attributes:d({},h.inner),children:[{tag:a.icon.tag,children:a.icon.children,attributes:d(d({},a.icon.attributes),h.path)}]}]}}}},Ze={x:0,y:0,width:"100%",height:"100%"};function wa(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:!0;return e.attributes&&(e.attributes.fill||t)&&(e.attributes.fill="black"),e}function zi(e){return e.tag==="g"?e.children:[e]}var Di={hooks:function(){return{parseNodeAttributes:function(n,a){var r=a.getAttribute("data-fa-mask"),o=r?oe(r.split(" ").map(function(i){return i.trim()})):He();return o.prefix||(o.prefix=it()),n.mask=o,n.maskId=a.getAttribute("data-fa-mask-id"),n}}},provides:function(t){t.generateAbstractMask=function(n){var a=n.children,r=n.attributes,o=n.main,i=n.mask,s=n.maskId,f=n.transform,l=o.width,u=o.icon,c=i.width,p=i.icon,h=Fr({transform:f,containerWidth:c,iconWidth:l}),m={tag:"rect",attributes:d(d({},Ze),{},{fill:"white"})},y=u.children?{children:u.children.map(wa)}:{},b={tag:"g",attributes:d({},h.inner),children:[wa(d({tag:u.tag,attributes:d(d({},u.attributes),h.path)},y))]},S={tag:"g",attributes:d({},h.outer),children:[b]},w="mask-".concat(s||Ft()),N="clip-".concat(s||Ft()),T={tag:"mask",attributes:d(d({},Ze),{},{id:w,maskUnits:"userSpaceOnUse",maskContentUnits:"userSpaceOnUse"}),children:[m,S]},M={tag:"defs",children:[{tag:"clipPath",attributes:{id:N},children:zi(p)},T]};return a.push(M,{tag:"rect",attributes:d({fill:"currentColor","clip-path":"url(#".concat(N,")"),mask:"url(#".concat(w,")")},Ze)}),{children:a,attributes:r}}}},Yi={provides:function(t){var n=!1;at.matchMedia&&(n=at.matchMedia("(prefers-reduced-motion: reduce)").matches),t.missingIconAbstract=function(){var a=[],r={fill:"currentColor"},o={attributeType:"XML",repeatCount:"indefinite",dur:"2s"};a.push({tag:"path",attributes:d(d({},r),{},{d:"M156.5,447.7l-12.6,29.5c-18.7-9.5-35.9-21.2-51.5-34.9l22.7-22.7C127.6,430.5,141.5,440,156.5,447.7z M40.6,272H8.5 c1.4,21.2,5.4,41.7,11.7,61.1L50,321.2C45.1,305.5,41.8,289,40.6,272z M40.6,240c1.4-18.8,5.2-37,11.1-54.1l-29.5-12.6 C14.7,194.3,10,216.7,8.5,240H40.6z M64.3,156.5c7.8-14.9,17.2-28.8,28.1-41.5L69.7,92.3c-13.7,15.6-25.5,32.8-34.9,51.5 L64.3,156.5z M397,419.6c-13.9,12-29.4,22.3-46.1,30.4l11.9,29.8c20.7-9.9,39.8-22.6,56.9-37.6L397,419.6z M115,92.4 c13.9-12,29.4-22.3,46.1-30.4l-11.9-29.8c-20.7,9.9-39.8,22.6-56.8,37.6L115,92.4z M447.7,355.5c-7.8,14.9-17.2,28.8-28.1,41.5 l22.7,22.7c13.7-15.6,25.5-32.9,34.9-51.5L447.7,355.5z M471.4,272c-1.4,18.8-5.2,37-11.1,54.1l29.5,12.6 c7.5-21.1,12.2-43.5,13.6-66.8H471.4z M321.2,462c-15.7,5-32.2,8.2-49.2,9.4v32.1c21.2-1.4,41.7-5.4,61.1-11.7L321.2,462z M240,471.4c-18.8-1.4-37-5.2-54.1-11.1l-12.6,29.5c21.1,7.5,43.5,12.2,66.8,13.6V471.4z M462,190.8c5,15.7,8.2,32.2,9.4,49.2h32.1 c-1.4-21.2-5.4-41.7-11.7-61.1L462,190.8z M92.4,397c-12-13.9-22.3-29.4-30.4-46.1l-29.8,11.9c9.9,20.7,22.6,39.8,37.6,56.9 L92.4,397z M272,40.6c18.8,1.4,36.9,5.2,54.1,11.1l12.6-29.5C317.7,14.7,295.3,10,272,8.5V40.6z M190.8,50 c15.7-5,32.2-8.2,49.2-9.4V8.5c-21.2,1.4-41.7,5.4-61.1,11.7L190.8,50z M442.3,92.3L419.6,115c12,13.9,22.3,29.4,30.5,46.1 l29.8-11.9C470,128.5,457.3,109.4,442.3,92.3z M397,92.4l22.7-22.7c-15.6-13.7-32.8-25.5-51.5-34.9l-12.6,29.5 C370.4,72.1,384.4,81.5,397,92.4z"})});var i=d(d({},o),{},{attributeName:"opacity"}),s={tag:"circle",attributes:d(d({},r),{},{cx:"256",cy:"364",r:"28"}),children:[]};return n||s.children.push({tag:"animate",attributes:d(d({},o),{},{attributeName:"r",values:"28;14;28;28;14;28;"})},{tag:"animate",attributes:d(d({},i),{},{values:"1;0;1;1;0;1;"})}),a.push(s),a.push({tag:"path",attributes:d(d({},r),{},{opacity:"1",d:"M263.7,312h-16c-6.6,0-12-5.4-12-12c0-71,77.4-63.9,77.4-107.8c0-20-17.8-40.2-57.4-40.2c-29.1,0-44.3,9.6-59.2,28.7 c-3.9,5-11.1,6-16.2,2.4l-13.1-9.2c-5.6-3.9-6.9-11.8-2.6-17.2c21.2-27.2,46.4-44.7,91.2-44.7c52.3,0,97.4,29.8,97.4,80.2 c0,67.6-77.4,63.5-77.4,107.8C275.7,306.6,270.3,312,263.7,312z"}),children:n?[]:[{tag:"animate",attributes:d(d({},i),{},{values:"1;0;0;0;0;1;"})}]}),n||a.push({tag:"path",attributes:d(d({},r),{},{opacity:"0",d:"M232.5,134.5l7,168c0.3,6.4,5.6,11.5,12,11.5h9c6.4,0,11.7-5.1,12-11.5l7-168c0.3-6.8-5.2-12.5-12-12.5h-23 C237.7,122,232.2,127.7,232.5,134.5z"}),children:[{tag:"animate",attributes:d(d({},i),{},{values:"0;0;1;1;0;0;"})}]}),{tag:"g",attributes:{class:"missing"},children:a}}}},Hi={hooks:function(){return{parseNodeAttributes:function(n,a){var r=a.getAttribute("data-fa-symbol"),o=r===null?!1:r===""?!0:r;return n.symbol=o,n}}}},Ui=[Yr,Oi,Ci,Ni,Pi,Li,Ri,Fi,Di,Yi,Hi];ei(Ui,{mixoutsTo:Y}),Y.noAuto,Y.config,Y.library,Y.dom;var $e=Y.parse;Y.findIconDefinition,Y.toHtml;var Wi=Y.icon;Y.layer,Y.text,Y.counter;let xa=!1;try{xa=process.env.NODE_ENV==="production"}catch{}function Vi(...e){!xa&&console&&typeof console.error=="function"&&console.error(...e)}function Aa(e){if(e&&typeof e=="object"&&e.prefix&&e.iconName&&e.icon)return e;if($e.icon)return $e.icon(e);if(e===null)return null;if(e&&typeof e=="object"&&e.prefix&&e.iconName)return e;if(Array.isArray(e)&&e.length===2)return{prefix:e[0],iconName:e[1]};if(typeof e=="string")return{prefix:"fas",iconName:e}}function tn(e,t){return Array.isArray(t)&&t.length>0||!Array.isArray(t)&&t?{[e]:t}:{}}function Bi(e){let t,n=[e[2]],a={};for(let r=0;r<n.length;r+=1)a=j(a,n[r]);return{c(){t=ge("svg"),un(t,a)},m(r,o){P(r,t,o),t.innerHTML=e[1],e[7](t)},p:E,i:E,o:E,d(r){r&&C(t),e[7](null)}}}function Gi(e,t,n){let{tag:a}=t,{props:r}=t,{children:o}=t,{style:i=null}=t,{ref:s=null}=t;if(a!=="svg")throw new Error('SvgElement requires a tag of "svg"');function f(m){return(m==null?void 0:m.reduce((y,b)=>y+(b.tag?l(b):b),""))||""}function l({tag:m,props:y,children:b}){const S=Object.keys(y).map(w=>`${w}="${y[w]}"`).join(" ");return`<${m} ${S}>${f(b)}</${m}>`}const u=f(o),c=r!=null&&r.style?`${r.style}${i||""}`:i,p={...r,style:c};function h(m){Ot[m?"unshift":"push"](()=>{s=m,n(0,s)})}return e.$$set=m=>{"tag"in m&&n(3,a=m.tag),"props"in m&&n(4,r=m.props),"children"in m&&n(5,o=m.children),"style"in m&&n(6,i=m.style),"ref"in m&&n(0,s=m.ref)},[s,u,p,a,r,o,i,h]}class Xi extends nt{constructor(t){super(),et(this,t,Gi,Bi,U,{tag:3,props:4,children:5,style:6,ref:0})}}function Ea(e){let t,n,a;const r=[e[2],{style:e[1]}];function o(s){e[28](s)}let i={};for(let s=0;s<r.length;s+=1)i=j(i,r[s]);return e[0]!==void 0&&(i.ref=e[0]),t=new Xi({props:i}),Ot.push(()=>Ka(t,"ref",o)),{c(){D(t.$$.fragment)},m(s,f){R(t,s,f),a=!0},p(s,f){const l=f[0]&6?Ct(r,[f[0]&4&&Bt(s[2]),f[0]&2&&{style:s[1]}]):{};!n&&f[0]&1&&(n=!0,l.ref=s[0],Ga(()=>n=!1)),t.$set(l)},i(s){a||(_(t.$$.fragment,s),a=!0)},o(s){k(t.$$.fragment,s),a=!1},d(s){F(t,s)}}}function qi(e){let t,n,a=e[2]&&Ea(e);return{c(){a&&a.c(),t=L()},m(r,o){a&&a.m(r,o),P(r,t,o),n=!0},p(r,o){r[2]?a?(a.p(r,o),o[0]&4&&_(a,1)):(a=Ea(r),a.c(),_(a,1),a.m(t.parentNode,t)):a&&(W(),k(a,1,1,()=>{a=null}),V())},i(r){n||(_(a),n=!0)},o(r){k(a),n=!1},d(r){r&&C(t),a&&a.d(r)}}}function Ki(e,t,n){const a=["border","mask","maskId","fixedWidth","inverse","flip","icon","listItem","pull","pulse","rotation","size","spin","spinPulse","spinReverse","beat","fade","beatFade","bounce","shake","symbol","title","titleId","transform","swapOpacity","ref","style"];let r=ln(t,a),{border:o=!1}=t,{mask:i=null}=t,{maskId:s=null}=t,{fixedWidth:f=!1}=t,{inverse:l=!1}=t,{flip:u=!1}=t,{icon:c=null}=t,{listItem:p=!1}=t,{pull:h=null}=t,{pulse:m=!1}=t,{rotation:y=null}=t,{size:b=null}=t,{spin:S=!1}=t,{spinPulse:w=!1}=t,{spinReverse:N=!1}=t,{beat:T=!1}=t,{fade:M=!1}=t,{beatFade:X=!1}=t,{bounce:q=!1}=t,{shake:At=!1}=t,{symbol:H=!1}=t,{title:Yt=""}=t,{titleId:an=null}=t,{transform:Ht=null}=t,{swapOpacity:Ca=!1}=t,{ref:me=null}=t,{style:Na=null}=t;const Pa=Aa(c),wo=tn("classes",[...sr(t),...(t.class||"").split(" ")]),xo=tn("transform",typeof Ht=="string"?$e.transform(Ht):Ht),Ao=tn("mask",Aa(i)),Ia=Wi(Pa,{...wo,...xo,...Ao,symbol:H,title:Yt,titleId:an,maskId:s});let Ta=null;if(!Ia)Vi("Could not find icon",Pa);else{const{abstract:v}=Ia;Ta=An((So,Oo,Co)=>({tag:So,props:Oo,children:Co}),v[0],r)}function Eo(v){me=v,n(0,me)}return e.$$set=v=>{n(35,t=j(j({},t),fn(v))),n(34,r=ln(t,a)),"border"in v&&n(3,o=v.border),"mask"in v&&n(4,i=v.mask),"maskId"in v&&n(5,s=v.maskId),"fixedWidth"in v&&n(6,f=v.fixedWidth),"inverse"in v&&n(7,l=v.inverse),"flip"in v&&n(8,u=v.flip),"icon"in v&&n(9,c=v.icon),"listItem"in v&&n(10,p=v.listItem),"pull"in v&&n(11,h=v.pull),"pulse"in v&&n(12,m=v.pulse),"rotation"in v&&n(13,y=v.rotation),"size"in v&&n(14,b=v.size),"spin"in v&&n(15,S=v.spin),"spinPulse"in v&&n(16,w=v.spinPulse),"spinReverse"in v&&n(17,N=v.spinReverse),"beat"in v&&n(18,T=v.beat),"fade"in v&&n(19,M=v.fade),"beatFade"in v&&n(20,X=v.beatFade),"bounce"in v&&n(21,q=v.bounce),"shake"in v&&n(22,At=v.shake),"symbol"in v&&n(23,H=v.symbol),"title"in v&&n(24,Yt=v.title),"titleId"in v&&n(25,an=v.titleId),"transform"in v&&n(26,Ht=v.transform),"swapOpacity"in v&&n(27,Ca=v.swapOpacity),"ref"in v&&n(0,me=v.ref),"style"in v&&n(1,Na=v.style)},t=fn(t),[me,Na,Ta,o,i,s,f,l,u,c,p,h,m,y,b,S,w,N,T,M,X,q,At,H,Yt,an,Ht,Ca,Eo]}class en extends nt{constructor(t){super(),et(this,t,Ki,qi,U,{border:3,mask:4,maskId:5,fixedWidth:6,inverse:7,flip:8,icon:9,listItem:10,pull:11,pulse:12,rotation:13,size:14,spin:15,spinPulse:16,spinReverse:17,beat:18,fade:19,beatFade:20,bounce:21,shake:22,symbol:23,title:24,titleId:25,transform:26,swapOpacity:27,ref:0,style:1},null,[-1,-1])}}var Ji={prefix:"fas",iconName:"arrow-right",icon:[448,512,[8594],"f061","M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"]},Qi={prefix:"fas",iconName:"up-right-from-square",icon:[512,512,["external-link-alt"],"f35d","M352 0c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9L370.7 96 201.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L416 141.3l41.4 41.4c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V32c0-17.7-14.3-32-32-32H352zM80 32C35.8 32 0 67.8 0 112V432c0 44.2 35.8 80 80 80H400c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32V432c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V112c0-8.8 7.2-16 16-16H192c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z"]},Zi=Qi,$i={prefix:"fas",iconName:"plus",icon:[448,512,[10133,61543,"add"],"2b","M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"]};let to={faArrowRight:Ji,faExternalLinkAlt:Zi,faPlus:$i},eo={},no={};const ao=ke(to),ro=ke(eo),io=ke(no);function oo(e){let t,n;const a=[{icon:e[3][e[0].icon_label]},e[4]];let r={};for(let o=0;o<a.length;o+=1)r=j(r,a[o]);return t=new en({props:r}),{c(){D(t.$$.fragment)},m(o,i){R(t,o,i),n=!0},p(o,i){const s=i&25?Ct(a,[i&9&&{icon:o[3][o[0].icon_label]},i&16&&Bt(o[4])]):{};t.$set(s)},i(o){n||(_(t.$$.fragment,o),n=!0)},o(o){k(t.$$.fragment,o),n=!1},d(o){F(t,o)}}}function so(e){let t,n;const a=[{icon:e[2][e[0].icon_label]},e[4]];let r={};for(let o=0;o<a.length;o+=1)r=j(r,a[o]);return t=new en({props:r}),{c(){D(t.$$.fragment)},m(o,i){R(t,o,i),n=!0},p(o,i){const s=i&21?Ct(a,[i&5&&{icon:o[2][o[0].icon_label]},i&16&&Bt(o[4])]):{};t.$set(s)},i(o){n||(_(t.$$.fragment,o),n=!0)},o(o){k(t.$$.fragment,o),n=!1},d(o){F(t,o)}}}function fo(e){let t,n;const a=[{icon:e[1][e[0].icon_label]},e[4]];let r={};for(let o=0;o<a.length;o+=1)r=j(r,a[o]);return t=new en({props:r}),{c(){D(t.$$.fragment)},m(o,i){R(t,o,i),n=!0},p(o,i){const s=i&19?Ct(a,[i&3&&{icon:o[1][o[0].icon_label]},i&16&&Bt(o[4])]):{};t.$set(s)},i(o){n||(_(t.$$.fragment,o),n=!0)},o(o){k(t.$$.fragment,o),n=!1},d(o){F(t,o)}}}function lo(e){let t,n,a,r;const o=[fo,so,oo],i=[];function s(f,l){return f[0].fa_group==="solid"?0:f[0].fa_group==="regular"?1:f[0].fa_group==="brands"?2:-1}return~(t=s(e))&&(n=i[t]=o[t](e)),{c(){n&&n.c(),a=L()},m(f,l){~t&&i[t].m(f,l),P(f,a,l),r=!0},p(f,[l]){let u=t;t=s(f),t===u?~t&&i[t].p(f,l):(n&&(W(),k(i[u],1,1,()=>{i[u]=null}),V()),~t?(n=i[t],n?n.p(f,l):(n=i[t]=o[t](f),n.c()),_(n,1),n.m(a.parentNode,a)):n=null)},i(f){r||(_(n),r=!0)},o(f){k(n),r=!1},d(f){f&&C(a),~t&&i[t].d(f)}}}function co(e,t,n){let a,r,o;Ut(e,ao,f=>n(1,a=f)),Ut(e,ro,f=>n(2,r=f)),Ut(e,io,f=>n(3,o=f));let{jp_props:i}=t;const s={...i.attrs,style:i.style,class:i.classes};return e.$$set=f=>{"jp_props"in f&&n(0,i=f.jp_props)},[i,a,r,o,s]}class uo extends nt{constructor(t){super(),et(this,t,co,lo,U,{jp_props:0})}}function mo(e){let t,n,a;var r=e[2][e[0].vue_type];function o(i,s){return{props:{jp_props:i[0],comp_ref:i[1]}}}return r&&(t=tt(r,o(e)),e[3](t)),{c(){t&&D(t.$$.fragment),n=L()},m(i,s){t&&R(t,i,s),P(i,n,s),a=!0},p(i,[s]){if(s&1&&r!==(r=i[2][i[0].vue_type])){if(t){W();const f=t;k(f.$$.fragment,1,0,()=>{F(f,1)}),V()}r?(t=tt(r,o(i)),i[3](t),D(t.$$.fragment),_(t.$$.fragment,1),R(t,n.parentNode,n)):t=null}else if(r){const f={};s&1&&(f.jp_props=i[0]),s&2&&(f.comp_ref=i[1]),t.$set(f)}},i(i){a||(t&&_(t.$$.fragment,i),a=!0)},o(i){t&&k(t.$$.fragment,i),a=!1},d(i){i&&C(n),e[3](null),t&&F(t,i)}}}function go(e,t,n){let a={html_component:_n,svg_component:xn,fontawesome_component:uo},{jp_props:r}=t,o;function i(s){Ot[s?"unshift":"push"](()=>{o=s,n(1,o)})}return e.$$set=s=>{"jp_props"in s&&n(0,r=s.jp_props)},[r,o,a,i]}class ue extends nt{constructor(t){super(),et(this,t,go,mo,U,{jp_props:0})}}const nn=we([]);function vo(e){nn.set(e)}function Sa(e,t,n){const a=e.slice();return a[1]=t[n],a}function Oa(e){let t,n,a;var r=ue;function o(i,s){return{props:{jp_props:i[1]}}}return r&&(t=tt(r,o(e))),{c(){t&&D(t.$$.fragment),n=L()},m(i,s){t&&R(t,i,s),P(i,n,s),a=!0},p(i,s){if(r!==(r=ue)){if(t){W();const f=t;k(f.$$.fragment,1,0,()=>{F(f,1)}),V()}r?(t=tt(r,o(i)),D(t.$$.fragment),_(t.$$.fragment,1),R(t,n.parentNode,n)):t=null}else if(r){const f={};s&1&&(f.jp_props=i[1]),t.$set(f)}},i(i){a||(t&&_(t.$$.fragment,i),a=!0)},o(i){t&&k(t.$$.fragment,i),a=!1},d(i){i&&C(n),t&&F(t,i)}}}function po(e){let t,n,a=bt(e[0]),r=[];for(let i=0;i<a.length;i+=1)r[i]=Oa(Sa(e,a,i));const o=i=>k(r[i],1,1,()=>{r[i]=null});return{c(){for(let i=0;i<r.length;i+=1)r[i].c();t=L()},m(i,s){for(let f=0;f<r.length;f+=1)r[f]&&r[f].m(i,s);P(i,t,s),n=!0},p(i,[s]){if(s&1){a=bt(i[0]);let f;for(f=0;f<a.length;f+=1){const l=Sa(i,a,f);r[f]?(r[f].p(l,s),_(r[f],1)):(r[f]=Oa(l),r[f].c(),_(r[f],1),r[f].m(t.parentNode,t))}for(W(),f=a.length;f<r.length;f+=1)o(f);V()}},i(i){if(!n){for(let s=0;s<a.length;s+=1)_(r[s]);n=!0}},o(i){r=r.filter(Boolean);for(let s=0;s<r.length;s+=1)k(r[s]);n=!1},d(i){i&&C(t),de(r,i)}}}function bo(e,t,n){let a;return Ut(e,nn,r=>n(0,a=r)),[a]}class ho extends nt{constructor(t){super(),et(this,t,bo,po,U,{})}}function yo(e){let t,n,a;return{c(){t=Wt("div"),n=La(),a=Wt("div"),Et(t,"class",e[0]),Et(a,"class","font-geist font-roboto")},m(r,o){P(r,t,o),P(r,n,o),P(r,a,o)},p:E,i:E,o:E,d(r){r&&(C(t),C(n),C(a))}}}function _o(e){return safe_twsty_arr=["[&_summary::-webkit-details-marker]:hidden","absolute ","bg-gradient-to-t ","bg-opacity-20","bg-pink-100 ","bg-pink-50/50 ","bg-primary-200","border ","border-gray-200 ","border-gray-300 ","border-gray-6 ","container ","cursor-pointer ","flex ","flex-1 ","flex-col ","focus:bg-primary-300","focus:outline-none ","focus:ring ","focus:shadow-ring-focus","focus:text-primary-600","font-bold ","font-medium","font-medium ","font-thin ","from-gray-200 ","gap-1 ","gap-1.5 ","gap-4 ","grid ","grid-cols-1 ","grid-flow-row ","grid-rows-2 ","group ","group-active:border-secondary-500","group-hover:text-secondary-600","h-5 ","h-max ","hover:bg-primary-400","hover:text-primary-600","invisible ","italic ","items-center ","justify-between ","justify-center ","justify-start ","lg:grid-cols-3 ","mb-2 ","mb-4 ","md:grid-cols-2 ","md:w-1/3 ","ml-4 ","ml-8 ","mt-0 ","mt-2 ","mt-4 ","mt-8 ","mx-auto ","overflow-auto ","p-1 ","p-2 ","p-4 ","pb-2 ","pl-2 ","pt-2 ","px-4 ","px-5 ","py-3 ","relative ","rounded-b-lg ","rounded-full","rounded-lg ","rounded-t-lg ","shadow-gray-2 ","shadow-gray-200 ","shadow-md ","shrink-0","sm:grid-cols-1 ","sm:max-md:hidden ","sm:max-md:w-full ","space-x-4 ","space-y-2 ","space-y-4 ","text ","text-2xl ","text-4xl ","text-6xl ","text-balance ","text-center ","text-gray-400 ","text-gray-600 ","text-gray-700 ","text-gray-800 ","text-gray-900 ","text-green-500 ","text-green-700 ","text-left ","text-lg ","text-pink-300 ","text-primary-700","text-purple-600 ","text-purple-700 ","text-red-600 ","text-rose-300 ","text-rose-500 ","text-slate-700 ","text-slate-700/50 ","text-sm ","text-xl ","to-gray-200 ","tracking-tight","tracking-tight ","transition-colors","transition-colors ","via-gray-100 ","w-1/2 ","w-2/3 ","w-5 ","w-full "],[safe_twsty_arr.join(" ")]}class ko extends nt{constructor(t){super(),et(this,t,_o,yo,U,{})}}return Za(),z.App=ho,z.TwSafelist=ko,z.justpyComponents=nn,z.setJustpyComponents=vo,z.updateComponentTwClass=tr,Object.defineProperty(z,Symbol.toStringTag,{value:"Module"}),z}({});
//# sourceMappingURL=bundle.iife.js.map
