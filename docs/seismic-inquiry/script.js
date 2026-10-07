
const progress = document.getElementById('progress');
const onScroll = () => {
  const h = document.documentElement;
  const p = h.scrollTop / (h.scrollHeight - h.clientHeight);
  progress.style.width = `${Math.max(0, Math.min(1, p))*100}%`;
};
addEventListener('scroll', onScroll, {passive:true}); onScroll();

const revealObserver = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('visible'); revealObserver.unobserve(e.target); }});
},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>revealObserver.observe(el));

const dlg = document.getElementById('lightbox');
const dlgImg = document.getElementById('lightboxImg');
const dlgCap = document.getElementById('lightboxCaption');
document.querySelectorAll('.photo-button').forEach(btn=>{
  btn.addEventListener('click',()=>{
    dlgImg.src = btn.dataset.src;
    dlgImg.alt = btn.dataset.caption || '';
    dlgCap.textContent = btn.dataset.caption || '';
    dlg.showModal();
  });
});
document.getElementById('lightboxClose').addEventListener('click',()=>dlg.close());
dlg.addEventListener('click',(e)=>{ if(e.target===dlg) dlg.close(); });

const shotLine = document.getElementById('shotLine');
let activeShot = 0;
shotPoints.forEach((s,i)=>{
  const b=document.createElement('button');
  b.className='shot-point'+(i===0?' active':'');
  b.innerHTML=`<span>S${s.n}</span><span class="pin"></span><small>${s.x} m</small>`;
  b.addEventListener('click',()=>{activeShot=i; updateShots();});
  shotLine.appendChild(b);
});
const receiverSlider=document.getElementById('receiverSlider');
const receiverValue=document.getElementById('receiverValue');
const distanceValue=document.getElementById('distanceValue');
const shotLabel=document.getElementById('shotLabel');
function updateShots(){
  document.querySelectorAll('.shot-point').forEach((b,i)=>b.classList.toggle('active',i===activeShot));
  const sx=shotPoints[activeShot].x, rx=+receiverSlider.value;
  receiverValue.textContent=rx;
  distanceValue.textContent=`${Math.abs(rx-sx)} m`;
  shotLabel.textContent=`S${activeShot+1} · ${sx} m`;
}
receiverSlider.addEventListener('input',updateShots); updateShots();

const svg=document.getElementById('travelChart');
const v1=document.getElementById('v1'), v2=document.getElementById('v2'), depth=document.getElementById('depth');
const v1Out=document.getElementById('v1Out'), v2Out=document.getElementById('v2Out'), hOut=document.getElementById('hOut');
const NS='http://www.w3.org/2000/svg';
const S=(tag,attrs={})=>{const e=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));return e;};
function travelTimes(x,V1,V2,h){
  const td=x/V1;
  if(V2<=V1) return {td,tr:Infinity};
  const ic=Math.asin(V1/V2);
  const ti=2*h*Math.cos(ic)/V1;
  return {td,tr:ti+x/V2};
}
function drawChart(){
  let V1=+v1.value, V2=+v2.value, h=+depth.value;
  if(V2<=V1+50){V2=V1+50;v2.value=V2;}
  v1Out.value=V1; v2Out.value=V2; hOut.value=h.toFixed(1);
  svg.innerHTML='';
  const W=760,H=420,m={l:70,r:26,t:34,b:58}, iw=W-m.l-m.r, ih=H-m.t-m.b;
  const xmax=60;
  let vals=[]; for(let x=0;x<=xmax;x+=1){const t=travelTimes(x,V1,V2,h);vals.push({x,...t});}
  const ymax=Math.max(...vals.filter(d=>isFinite(d.tr)).flatMap(d=>[d.td,d.tr]))*1.08;
  const X=x=>m.l+x/xmax*iw, Y=t=>m.t+ih-t/ymax*ih;
  const grid=S('g'); svg.appendChild(grid);
  for(let i=0;i<=6;i++){
    const x=i*10; grid.appendChild(S('line',{x1:X(x),y1:m.t,x2:X(x),y2:m.t+ih,stroke:'#e8e8e2','stroke-width':'1'}));
    const tx=S('text',{x:X(x),y:H-25,'text-anchor':'middle',fill:'#6f7874','font-size':'12'});tx.textContent=x;svg.appendChild(tx);
  }
  for(let i=0;i<=4;i++){
    const t=ymax*i/4; grid.appendChild(S('line',{x1:m.l,y1:Y(t),x2:W-m.r,y2:Y(t),stroke:'#ecece7','stroke-width':'1'}));
    const ty=S('text',{x:m.l-12,y:Y(t)+4,'text-anchor':'end',fill:'#6f7874','font-size':'12'});ty.textContent=(t*1000).toFixed(0);svg.appendChild(ty);
  }
  svg.appendChild(S('line',{x1:m.l,y1:m.t,x2:m.l,y2:m.t+ih,stroke:'#88918d','stroke-width':'1.4'}));
  svg.appendChild(S('line',{x1:m.l,y1:m.t+ih,x2:W-m.r,y2:m.t+ih,stroke:'#88918d','stroke-width':'1.4'}));
  const xlabel=S('text',{x:m.l+iw/2,y:H-5,'text-anchor':'middle',fill:'#43504a','font-size':'13','font-weight':'700'});xlabel.textContent='Distance (m)';svg.appendChild(xlabel);
  const ylabel=S('text',{x:18,y:m.t+ih/2,transform:`rotate(-90 18 ${m.t+ih/2})`,'text-anchor':'middle',fill:'#43504a','font-size':'13','font-weight':'700'});ylabel.textContent='Travel time (ms)';svg.appendChild(ylabel);
  const makePath=(key,color,dash='')=>{
    let d=vals.map((p,i)=>`${i?'L':'M'} ${X(p.x).toFixed(1)} ${Y(p[key]).toFixed(1)}`).join(' ');
    svg.appendChild(S('path',{d,fill:'none',stroke:color,'stroke-width':'3','stroke-dasharray':dash}));
  };
  makePath('td','#557a69');
  makePath('tr','#d69a49','7 6');
  let first=vals.map((p,i)=>`${i?'L':'M'} ${X(p.x).toFixed(1)} ${Y(Math.min(p.td,p.tr)).toFixed(1)}`).join(' ');
  svg.appendChild(S('path',{d:first,fill:'none',stroke:'#d96a3a','stroke-width':'4'}));
  const ic=Math.asin(V1/V2), ti=2*h*Math.cos(ic)/V1;
  const denom=(1/V1-1/V2);
  const xc=denom>0?ti/denom:Infinity;
  if(xc<=xmax){
    svg.appendChild(S('line',{x1:X(xc),y1:m.t,x2:X(xc),y2:m.t+ih,stroke:'#c9c9c2','stroke-width':'1.5','stroke-dasharray':'4 5'}));
    const c=S('text',{x:X(xc)+8,y:m.t+18,fill:'#6a716e','font-size':'12'});c.textContent=`crossover ≈ ${xc.toFixed(1)} m`;svg.appendChild(c);
  }
  const title=S('text',{x:m.l,y:20,fill:'#1d2c26','font-size':'14','font-weight':'800'});
  title.textContent=`Two-layer teaching model · V₁=${V1} m/s · V₂=${V2} m/s · h=${h.toFixed(1)} m`;
  svg.appendChild(title);
}
[v1,v2,depth].forEach(el=>el.addEventListener('input',drawChart)); drawChart();
