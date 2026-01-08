function addTwo(num: number): number {
  return num + 2;
}

// function getValue(myVal: number): boolean {
//   if (myVal > 5) {
//     return true;
//   }
//   return "200 ok"
// }

const getHello = (s: string): string => {
  return "";
}

const heroes = ["thor", "spider man", "iron man"];
// const heroes = [1, 2, 3];

heroes.map((hero): string => {
  return `hero is ${hero}`
})

function consoleError(errmsg: string): void {
  console.log(errmsg);
}

export {}