class ThreeSample {
    constructor() {
      //シーン作成
      this.threeScene = new THREE.Scene();
      //カメラ作成
      this.threeCamera = new THREE.PerspectiveCamera(45, 600 / 250, 0.1, 2500);
      //シーンにカメラを追加
      this.threeScene.add(this.threeCamera);
      //レンダーを作成
      this.threeRender = new THREE.WebGLRenderer({ antialias: true });
      //レンダーのバックグラウンドカラー 色 α
      this.threeRender.setClearColor(0x000000, 1);
      //レンダーのサイズ
      this.threeRender.setSize(600, 250);
      //カメラの位置
      this.threeCamera.position.set(-300, 500, 500);
      //カメラの向き
      this.threeCamera.lookAt(this.threeScene.position);
      //threejsのレンダーをpixijsのテクスチャに
      this.threeTexture = PIXI.BaseTexture.from(
        this.threeRender.domElement,
        PIXI.SCALE_MODES.LINEAR
      );
      //pixijsのスプライトに
      this.threeSprite = new PIXI.Sprite.from(
        new PIXI.Texture(this.threeTexture)
      );
      this.threeSprite.x = 25;
      this.threeSprite.y = 50;
      //pixijsのステージに追加
      app.stage.addChild(this.threeSprite);
      //球体のサイズ
      this.radius = 300;
      this.sp = 1;
      this.line_material = new THREE.LineBasicMaterial({ color: 0xffffff });
    }
    //index.htmlのpixiティッカーで更新している
    tick() {
      //ラインがあれば消去
      this.threeScene.remove(this.newline);
      //ラインを作成
      var line_geometry = new THREE.Geometry();
      let s = 0;
      let t = 0;
      let lastX = 0;
      let lastY = 0;
      let lastZ = 0;
      this.sp += 0.05;
      while (t < 180) {
        s += this.sp;
        t += 0.5;
        let radianS = s * (Math.PI / 180);
        let radianT = t * (Math.PI / 180);
        let thisX = 0 + this.radius * Math.cos(radianS) * Math.sin(radianT);
        let thisY = 0 + this.radius * Math.sin(radianS) * Math.sin(radianT);
        let thisZ = 0 + this.radius * Math.cos(radianT);
        if (lastX != 0) {
          line_geometry.vertices.push(
            new THREE.Vector3(thisX, thisY, thisZ),
            new THREE.Vector3(lastX, lastY, lastZ)
          );
        }
        lastX = thisX;
        lastY = thisY;
        lastZ = thisZ;
      }
      this.newline = new THREE.Line(line_geometry, this.line_material);
      this.threeScene.add(this.newline);
      this.threeRender.render(this.threeScene, this.threeCamera);
      this.threeTexture.update();
    }
  }
  