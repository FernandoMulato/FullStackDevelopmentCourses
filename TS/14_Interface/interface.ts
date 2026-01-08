interface User {
  readonly dbId: number,
  email: string,
  userId: number,
  googleId?: string,
  // startTrail: () => string
  startTrail(): string,
  getCoupon(couponName: string, value: number): number
}

const fernando: User = {
  dbId: 22,
  email: "sds@cc.com",
  userId: 111,
  startTrail: () => {
    return "trail started";
  },
  getCoupon: (name: "fernando10", off: 10) => {
    return 10;
  } 
}

fernando.email = "sds@cc.com"
// fernando.dbId = 111;

export {}