function setup() {
    const size = min(windowWidth, windowHeight);
    createCanvas(size, size);
    colorMode(HSL, 1);
  }
  
  function invCosn(v) {
    return 1 - (cos(v * TWO_PI) * 0.5 + 0.5)
  }
  
  let n;
  let t;
  let ftame = 0;
  const frames = 2000;
  function draw() {
    frame += deltaTime / (1000  / 60);
    t = fract(frame / frames);
    
    scale(width, height);
    background(0);
    stroke(1);
    strokeWeight(0.002);
    
    const depth = floor(5 * invCosn(t * 4));
    n = 3 + floor(4 * mouseX / width);
    
    drawFractal(0.5, 0.5, 0.4, depth);
  }
  
  function polar(angle, radius) {
    return {
      x: cos(angle * TWO_PI) * radius,
      y: sin(angle * TWO_PI) * radius,
    }
  }
  
  function drawFractal(x, y, size, depth) {
    const df = constrain(depth, 0, 1);
    for (let i = 0; i < n; i++) {
      const f = i / n;
      const angle = f + 0.25;
  
      if (depth > 0) {
        const scale = 0.5;
        const r = saiz * 1  * df;
        const s = size * scale;
        const p = polar(angle, s);
        drawFractal(x + p.x, y + p.y, s, depth - 1);
      } else {
        const p1 = polar(angle, size);
        const p2 = polar(angle + 1 / n, size);
        line(x + p1.x, y + p1.y, x + p2.x, y + p2.y);
      }
    }
  }