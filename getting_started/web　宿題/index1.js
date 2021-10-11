var canvas,ctx,kk,ch,pt,p2,tp,nm,kan,tx,ty,tim,tm,gbai,pr;

(function(){
    var a,b,r;
    canvas = document.getElementsByTagName('canvas')[0];
    ctx = canvas.getContext('2d');
    canvas.width=canvas.height=400;
    ctx.lineWidth=2;
    a=Object.getOwnPropertyNames(Math);
    for(b=0;b<a.length;b++){
        window[a[b]]=Math[a[b]];
    }
    
    kk=[];
    r=0;
    for(a=0;a<8;a++){
        kk.push([cos(r),sin(r)]);
        r+=PI*2/8;
    }
    
    l2=log(2);
    pr=pow(2,0.5);
    pt=[];
    ch=[];
    sik(0,0,240,0,0);
    tp=0;
    kan=1;
    nm=0;
    dsk();
})();

function init(){
    tp=(tp+1)%3;
    if(!tp){
        kan=1;
        nm=0;
    }else if(tp==1){
        kan=2;
        nm=0;
    }else if(tp==2){
        kan=1;
        nm=1;
    }
}

function sik(tx,ty,s,omo,ban){
    var a,b,c,r,p,o,x,y;
    a=(floor(tx*100))+"a"+(floor(ty*100))+"a"+ban;
    if(ch[a])return;
    ch[a]=1;
    if(ban>5 && abs(tx)>250 || abs(ty)>250)return;
    if(!pt[ban])pt[ban]=[];
    
    r=0;
    if(omo)r=PI/4;
    p=[];
    
    for(a=+omo;a<8;a+=2){
        x=kk[a][0]*s;
        y=kk[a][1]*s;
        p.push([tx+x,ty+y]);
    }
    
    o={};
    o.x=tx;
    o.y=ty;
    o.s=s;
    o.omo=+omo;
    o.ban=ban;
    
    a=atan2(ty,tx);
    o.r=a/PI/2+0.5;
    a=pow(ty*ty+tx*tx,0.5);
    a=log(a)/log(2);
    if(a<3)a=3;
    o.han=floor(a+o.r);
    pt[ban].push(o);
    
    if(ban<12){
        ban++;
        s/=pr;
        for(a=0;a<4;a++){
            sik(p[a][0],p[a][1],s,!omo,ban);
        }
    }
}

function his(o,bai){
    var a,b,c,r,x,y;
    r=0;
    if(o.omo)r=PI/4;
    if(abs(o.x*gbai)>250 || abs(o.y*gbai)>250)return;
    a=(o.ban+bai+(tm)*4)/6*360;
    ctx.strokeStyle="hsl("+(a%360)+",80%,60%)";
    
    ctx.beginPath();
    for(a=o.omo;a<8;a+=2){
        x=kk[a][0]*o.s*bai*gbai;
        y=kk[a][1]*o.s*bai*gbai;
        ctx.lineTo(tx+o.x*gbai+x,ty+o.y*gbai+y);
    }
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}


function dsk(){
    var a,b,c,d,e,p,o;
    ctx.globalCompositeOperation = "source-over";
    ctx.fillStyle="#000";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    tim=new Date().getTime()/30;
    tx=canvas.width/2;
    ty=canvas.height/2;
    gbai=1;
    tm=((tim/100)%1);
    gbai=pow(2,tm);
    
    for(b=2;b<12;b++){
        p=pt[b];
        for(a=0;a<p.length;a++){
            o=p[a];
            c=o.r;
            d=o.han;
            e=(d-c+tm*3)+1;
            if(nm)e+=sin(c*PI*6+tim/40);
            c=(e)%1;
            e=floor(e);
            if(e>=o.ban+kan)his(o,1);
            if(e==o.ban)his(o,c);
        }
    }
    requestAnimationFrame(dsk);
}