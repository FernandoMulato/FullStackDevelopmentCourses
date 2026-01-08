let score: number | string = 33;

score = 44;

score = "55";

type User = {
  name: string;
  id: number;
}

type Admin = {
  username: string;
  id: number;
}

let fernando: User | Admin = {name: "Fernando", id: 133};

fernando = {username: "fm", id: 131}

// function getDbId(id: number | string) {
//   // making some API calls
//   console.log(`Db id is: ${id}`);
// }

getDbId(3);
getDbId("3");
function getDbId(id: number | string) {
  if (typeof id === "string") {
    id.toLowerCase();
  } else {
    id.toExponential(5);
  }
}

// Array
const data: (number | string | boolean)[] = [1, 2, 3, "4", true];

let seatAllotment: "aisle" | "middle" | "window";

seatAllotment = "aisle";
// seatAllotment = "crew";

export {}