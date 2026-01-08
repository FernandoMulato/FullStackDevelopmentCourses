interface User {
  readonly dbId: number,
  email: string,
  userId: number,
  googleId?: string,
  // startTrail: () => string,
  startTrail(): string,
  getCoupon(couponName: string, value: number): number
}

interface User {
  githubToken: string
}

interface Admin extends User {
  role: "admin" | "ta" | "leaner"
}

const fernando: Admin = {
  dbId: 22,
  email: "sds@cc.com",
  userId: 111,
  githubToken: "github",
  role: "admin",
  startTrail: () => {
    return "trail started";
  },
  getCoupon: (name: "fernando10", off: 10) => {
    return 10;
  } 
}
export {}