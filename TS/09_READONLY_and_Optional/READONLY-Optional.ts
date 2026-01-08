type User = {
  readonly _id: string;
  name: string;
  email: string;
  isActive: boolean;
  // Optional (?)
  credcardDetails?: number;
}

let myUser: User = {
  _id: "1234",
  name: "h",
  email: "ds@gm.com",
  isActive: false
} 

myUser.email = "ss@gma.com";
// myUser._id = "1111";

type cardNumber = {
  cardNumber: string;
}

type cardDate = {
  cardDate: string;
}

type cardDetails = cardNumber & cardDate & {
  cvv: number;
};

export {}