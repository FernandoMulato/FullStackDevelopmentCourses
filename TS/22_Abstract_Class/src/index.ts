abstract class TakePhoto {
  constructor(
    public cameraMode: string,
    public filter: string
  ) {}

  abstract getSepia(): void;
  getReelTime() : number {
    // Some complex calculation
    return 8;
  }
}

// const obj = new TakePhoto("test", "test");

class Instagram extends TakePhoto {
  constructor(
    public cameraMode: string,
    public filter: string,
    public burst: number
  ) {
    super(cameraMode, filter)
  }

  getSepia(): void {
    console.log("Sepia");
    
  }
}

const obj = new Instagram("test", "test", 3);

obj.getReelTime();


