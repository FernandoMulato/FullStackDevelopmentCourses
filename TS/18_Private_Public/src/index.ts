// class User {

//   public email: string;
//   private name: string;
//   readonly city: string = "New York";

//   constructor(email: string, name: string) {
//     this.email = email;
//     this.name = name;
//   }
// }

class User {
  readonly city: string = "New York";
  constructor(
    public email: string,
    public name: string,
    // private userId: string
  ) {
  }
}

const fernando = new User("gdg@gh.com", "fernando");
fernando.name = "New user";