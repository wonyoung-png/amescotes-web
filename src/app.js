gsap.registerPlugin(ScrollTrigger);
const lenis=new Lenis({lerp:.09}); lenis.on('scroll',ScrollTrigger.update);
gsap.ticker.add(t=>lenis.raf(t*1000)); gsap.ticker.lagSmoothing(0);
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const wide=()=>innerWidth>820, body=document.body, clamp=gsap.utils.clamp(0,1);

// shapes chapters are built from data so the tab bar and chapters stay in sync
const SHAPES=C.services.map((t,i)=>({...C.site.chapters[i],...t}));
$('#works').innerHTML=SHAPES.map((x,i)=>`<div class="ch${x.dark?' dark':''}" id="ch${i}"><div class="sticky" style="background:${x.bg}">
  <h2 class="disp">${x.name}</h2><p class="say">${x.say}</p>
  <div class="prod"><img src="${x.image}" alt="${x.name}">${x.hotspots.map(h=>`<span class="hot" style="left:${h[0]}%;top:${h[1]}%">+</span>`).join('')}</div>
  <div class="feat">${x.features.map(f=>`<div><b>${f[0]}</b><p>${f[1]}</p></div>`).join('')}</div>
  <div class="stats mono">${x.stats.map(s=>`<div><span>${s[0]}</span><span>${s[1]}</span></div>`).join('')}</div></div></div>`).join('');
const bar=document.createElement('div');bar.id='shapebar';bar.className='mono';
bar.innerHTML=SHAPES.map((x,i)=>`<button data-i="${i}"><img src="${x.image}" alt="">${x.tab}</button>`).join('');body.appendChild(bar);
bar.querySelectorAll('button').forEach(b=>b.onclick=()=>lenis.scrollTo('#ch'+b.dataset.i,{duration:1.2}));

// loader -> hero
gsap.timeline()
  .to('#loader img',{opacity:0,duration:.4,delay:.9})
  .to('#loader',{yPercent:-100,duration:.8,ease:'power4.inOut'})
  .add(()=>{if(wide())body.classList.remove('drawer-closed')},'-=.5')
  .from('.hero .bg',{scale:1.15,duration:1.6,ease:'power3.out'},'-=.6')
  .to('.hero h1 .ln>span',{y:0,duration:1.1,stagger:.12,ease:'power4.out'},'-=1.3')
  .from(['.hero .btn','.hero .sub'],{opacity:0,duration:.6},'-=.6');

// drawer: open on the hero, folds into the right-edge handle after
ScrollTrigger.create({trigger:'.hero',start:'top top',end:'bottom 70%',onLeave:()=>body.classList.add('drawer-closed'),onEnterBack:()=>{if(wide())body.classList.remove('drawer-closed')}});
$('#handle').onclick=()=>body.classList.remove('drawer-closed');
$$('[data-go]').forEach(a=>a.onclick=e=>{e.preventDefault();lenis.scrollTo('#'+a.dataset.go,{duration:1.4});if(a.dataset.go!=='hero')setTimeout(()=>body.classList.add('drawer-closed'),300)});
document.addEventListener('click',e=>{if(!e.target.closest('#drawer,#handle')&&scrollY>innerHeight*.5)body.classList.add('drawer-closed')});

// story: camera pushes in, one sentence at a time, its cards pop in
const lis=$$('#story li'),cards=$$('#story .card');
ScrollTrigger.create({trigger:'#story',start:'top top',end:'bottom bottom',onUpdate(st){
  const p=st.progress,n=lis.length,i=Math.min(n-1,Math.floor(p/.86*n)),end=p>.86;
  gsap.set('#story .bg',{scale:1+p*.35});
  lis.forEach((l,j)=>l.classList.toggle('on',!end&&j===i));
  cards.forEach(c=>c.classList.toggle('on',!end&&+c.dataset.i===i));
  gsap.set('#story ul',{opacity:end?0:1});gsap.set('#story .end',{opacity:end?clamp((p-.86)/.06):0});
}});

// unfold: small photo grows to full bleed, titles swap, columns rise
const imgs=$$('#unfold .win img'),tts=$$('#unfold .tt span');
ScrollTrigger.create({trigger:'#unfold',start:'top top',end:'bottom bottom',onUpdate(st){
  const p=st.progress,g=clamp(p/.35),e=gsap.parseEase('power2.inOut')(g),c=clamp((p-.4)/.1),I=gsap.utils.interpolate;
  const SB=$('#unfold .sticky'),SW=SB.clientWidth,SH=SB.clientHeight;
  gsap.set('#unfold .win',{width:I(SW*(wide()?.34:.7),SW,e),height:I(SH*.34,SH,e),top:I(SH*.56,SH*.5,e),borderRadius:6*(1-e),'--dim':e});
  unfoldDark=g>.6;
  gsap.set('#unfold .t0',{opacity:1-g*2.2,y:-g*60});gsap.set('#unfold .tt',{opacity:g>.9?1:0});
  const k=p<.55?0:p<.78?1:2;tts.forEach((t,j)=>t.classList.toggle('on',j===k));imgs.forEach((m,j)=>m.classList.toggle('on',j===k));
  gsap.set('#unfold .cols',{opacity:c,y:30*(1-c)});
}});

// shapes: product rises and grows with scroll, details draw in after
SHAPES.forEach((x,i)=>{const ch=$('#ch'+i);
  ScrollTrigger.create({trigger:ch,start:'top top',end:'bottom bottom',onUpdate(st){
    const p=st.progress,a=clamp(p/.45),b=clamp((p-.45)/.2);
    gsap.set(ch.querySelector('.prod'),{yPercent:-50+40*(1-a),scale:.55+.55*a,rotation:-8*(1-a)});
    gsap.set(ch.querySelector('h2'),{opacity:1-b*.85});
    gsap.set(ch.querySelectorAll('.feat,.stats'),{opacity:b,y:20*(1-b)});
    ch.querySelectorAll('.hot').forEach((h,j)=>gsap.set(h,{opacity:clamp((p-.55-j*.08)/.08)}));
  },onToggle(st){if(st.isActive)bar.querySelectorAll('button').forEach((b,j)=>b.classList.toggle('on',j===i))}});
});
ScrollTrigger.create({trigger:'#works',start:'top 60%',end:'bottom 40%',toggleClass:{targets:'#shapebar',className:'on'}});

// globe: drag to rotate, tap a point to fly there
const PLACES=C.site.places.map((p,i)=>({...p,...C.global.places[i]}));
(async()=>{
  const el=$('#globe'),svg=d3.select(el);
  const world=await fetch('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-110m.json').then(r=>r.json());
  const land=topojson.feature(world,world.objects.land);
  const proj=d3.geoOrthographic().rotate([-122,-22]).clipAngle(90),path=d3.geoPath(proj);
  const sphere=svg.append('path').datum({type:'Sphere'}).attr('fill','rgba(255,255,255,.06)').attr('stroke','rgba(255,255,255,.18)');
  const grat=svg.append('path').datum(d3.geoGraticule10()).attr('fill','none').attr('stroke','rgba(255,255,255,.08)');
  const lnd=svg.append('path').datum(land).attr('fill','#5EA38F').attr('stroke','#8DBDAF').attr('stroke-width',.5);
  const arcs=svg.append('g'),pts=svg.append('g');
  let filter='all',active=0;
  const size=()=>{const w=el.clientWidth,h=el.clientHeight;proj.scale(Math.min(w,h)*.46).translate([w*.55,h*.62])};
  function draw(){
    sphere.attr('d',path);grat.attr('d',path);lnd.attr('d',path);
    const vis=PLACES.filter(p=>filter==='all'||p.f===filter),center=proj.invert(proj.translate());
    arcs.selectAll('path').data(vis.filter(p=>p!==PLACES[0])).join('path')
      .attr('d',p=>path({type:'LineString',coordinates:[PLACES[0].c,p.c]})).attr('fill','none').attr('stroke','#fff').attr('stroke-opacity',.45).attr('stroke-dasharray','3 4');
    pts.selectAll('g').data(vis,d=>d.n).join(e=>{const q=e.append('g').style('cursor','pointer').on('click',(ev,d)=>pick(PLACES.indexOf(d)));q.append('circle').attr('class','halo');q.append('circle').attr('class','dot');q.append('text');return q})
      .each(function(d){const [x,y]=proj(d.c),a=PLACES.indexOf(d)===active,s=d3.select(this);
        s.attr('transform',`translate(${x},${y})`).style('display',d3.geoDistance(d.c,center)<Math.PI/2?null:'none');
        s.select('.halo').attr('r',a?18:12).attr('fill','none').attr('stroke',a?'#fff':'#FBEBD8').attr('stroke-dasharray','2 3');
        s.select('.dot').attr('r',5).attr('fill',a?'#fff':'#163A30').attr('stroke','#fff').attr('stroke-width',1.5);
        s.select('text').text(d.n).attr('x',d.o[0]).attr('y',d.o[1]).attr('fill','#fff').attr('font-family','IBM Plex Mono').attr('font-size',12).attr('font-size',13)})}
  function pick(i){active=i;const d=PLACES[i];$('#mc-k').textContent=d.k;$('#mc-h').textContent=d.n;$('#mc-p').textContent=d.p;
    const ip=d3.interpolate(proj.rotate(),[-d.c[0]+6,-d.c[1]+10]);d3.transition().duration(900).tween('r',()=>t=>{proj.rotate(ip(t));draw()})}
  svg.call(d3.drag().on('drag',e=>{const r=proj.rotate(),k=70/proj.scale();proj.rotate([r[0]+e.dx*k,Math.max(-60,Math.min(60,r[1]-e.dy*k))]);draw()}));
  $$('#map-tabs button').forEach(b=>b.onclick=()=>{$$('#map-tabs button').forEach(x=>x.classList.remove('on'));b.classList.add('on');filter=b.dataset.f;pick(PLACES.findIndex(p=>filter==='all'||p.f===filter))});
  addEventListener('resize',()=>{size();draw()});size();draw();pick(0);
})();

// reveals + marquee speed
gsap.utils.toArray('.clients h2,.range h2,.journal h2,.rg>div,.journal a,form').forEach(el=>gsap.from(el,{y:50,opacity:0,duration:1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%'}}));

// footer odometer: CSS px -> metres (96px = 1 inch), stitches at 9 per inch
let travelled=0,last=scrollY;
lenis.on('scroll',()=>{travelled+=Math.abs(scrollY-last);last=scrollY;const inch=travelled/96;
  $('#odo-m').textContent=(inch*.0254).toFixed(1)+' m';$('#odo-s').textContent=Math.round(inch*9).toLocaleString('en-US')+' '+C.footer.unit});
gsap.from('footer .bag',{yPercent:30,rotation:12,ease:'none',scrollTrigger:{trigger:'footer',start:'top bottom',end:'top top',scrub:true}});

// form segmented control
$$('.seg span').forEach(s=>s.onclick=()=>{s.parentNode.querySelectorAll('span').forEach(x=>x.classList.remove('on'));s.classList.add('on')});

// contact form -> email (endpoint in content/site.json)
const form=$('#contact form');
form.addEventListener('submit',async e=>{e.preventDefault();const btn=form.querySelector('button'),fd=new FormData(form);
  fd.set('희망 생산지 / site',form.querySelector('.seg .on').textContent);fd.set('_subject','[홈페이지 문의] '+(fd.get('company')||''));fd.set('_template','table');fd.set('_captcha','false');
  btn.disabled=true;btn.textContent=C.contact.sending;
  try{const r=await fetch(C.site.form_endpoint,{method:'POST',headers:{Accept:'application/json'},body:fd});if(!r.ok)throw 0;btn.textContent=C.contact.sent;form.reset()}
  catch(_){btn.disabled=false;btn.textContent=C.contact.error}});

// gallery: films play only on screen, filter, lightbox (arrows / keys / swipe)
const gItems=$$('#gg .it');
const gio=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){if(!v.src)v.src=v.dataset.src;v.play().catch(()=>{})}else v.pause()}),{rootMargin:'200px'});
$$('#gg video').forEach(v=>gio.observe(v));
// show a first batch, MORE reveals the next one (desktop 16, mobile 10)
const STEP=()=>innerWidth>820?16:10;let shown=STEP();
function gpaint(){let n=0;gItems.forEach(it=>{const v=!it.classList.contains('hide');it.classList.toggle('cut',v&&++n>shown)});
  const total=gItems.filter(it=>!it.classList.contains('hide')).length;$('#gcount').textContent=Math.min(shown,total)+' / '+total;
  $('.gmore').classList.toggle('done',shown>=total);ScrollTrigger.refresh()}
$('#gmore').onclick=()=>{shown+=STEP();gpaint()};
$$('#gf button').forEach(b=>b.onclick=()=>{$$('#gf button').forEach(x=>x.classList.toggle('on',x===b));gItems.forEach(it=>it.classList.toggle('hide',b.dataset.t!=='all'&&it.dataset.t!==b.dataset.t));shown=STEP();gpaint()});
gpaint();
const lb=$('#lb'),lbm=$('#lbm');let cur=-1;
document.body.appendChild(lb);
const gvis=()=>gItems.filter(it=>!it.classList.contains('hide')).map(it=>+it.dataset.i);  // lightbox browses the whole filtered set, not just the revealed batch
function gshow(i){cur=i;const g=G[i];lbm.innerHTML=g.type==='photo'?`<img src="gallery/${g.id}.jpg" alt="">`:`<video src="gallery/${g.id}.mp4" autoplay muted loop playsinline controls></video>`;
  const v=gvis();$('#lbn').textContent=(v.indexOf(i)+1)+' / '+v.length;lb.classList.add('on');lenis.stop()}
function gstep(d){const v=gvis();gshow(v[(v.indexOf(cur)+d+v.length)%v.length])}
function gclose(){lb.classList.remove('on');lbm.innerHTML='';lenis.start()}
gItems.forEach(it=>it.onclick=()=>gshow(+it.dataset.i));
lb.querySelector('.x').onclick=gclose;lb.querySelector('.pv').onclick=()=>gstep(-1);lb.querySelector('.nx').onclick=()=>gstep(1);
lb.onclick=e=>{if(e.target===lb||e.target===lbm)gclose()};
addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')gclose();if(e.key==='ArrowRight')gstep(1);if(e.key==='ArrowLeft')gstep(-1)});
let gsx=0;lb.addEventListener('touchstart',e=>gsx=e.touches[0].clientX,{passive:true});lb.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-gsx;if(Math.abs(dx)>50)gstep(dx<0?1:-1)});

// client rows: auto drift (row 1 → left, row 2 → right); dragging or swiping moves both rows with the finger
(()=>{const box=$('#rows');if(!box)return;const tr=[...box.querySelectorAll('.track')];
  const st=tr.map(t=>({el:t,x:0,dir:+t.dataset.dir,half:()=>t.scrollWidth/2}));
  let drag=false,last=0,vel=0,hover=false;const SPEED=.45;
  const wrap=s=>{const h=s.half();s.x=((s.x%h)+h)%h-h};
  st[1].x=-st[1].half()/2;
  gsap.ticker.add(()=>{const auto=drag?0:(hover?SPEED*.25:SPEED);
    st.forEach(s=>{s.x+= -s.dir*auto+ (drag?0:vel);wrap(s);s.el.style.transform=`translate3d(${s.x}px,0,0)`});vel*=.92});
  box.addEventListener('pointerdown',e=>{drag=true;last=e.clientX;vel=0;box.classList.add('drag');box.setPointerCapture(e.pointerId)});
  box.addEventListener('pointermove',e=>{if(!drag)return;const dx=e.clientX-last;last=e.clientX;vel=dx;st.forEach(s=>{s.x+=dx;wrap(s)})});
  const up=()=>{drag=false;box.classList.remove('drag')};box.addEventListener('pointerup',up);box.addEventListener('pointercancel',up);
  box.addEventListener('mouseenter',()=>hover=true);box.addEventListener('mouseleave',()=>{hover=false;up()});
})();

// logo colour follows what is behind it: white over photos / dark sections, ink over light ones
let unfoldDark=false;
const DARK=new Set(['hero','story','map','contact','ch2']);
function logoTone(){const y=28;let dark=false;
  for(const el of document.querySelectorAll('#works > .ch, body > section:not(#works), footer')){const r=el.getBoundingClientRect();if(r.top<=y&&r.bottom>y){dark=el.id==='unfold'?unfoldDark:DARK.has(el.id);break}}
  document.querySelector('.logo-fixed').classList.toggle('on-light',!dark)}
lenis.on('scroll',logoTone);addEventListener('load',logoTone);logoTone();
