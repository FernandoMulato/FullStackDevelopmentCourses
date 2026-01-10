class User {

  email: string;
  name: string;
  readonly city: string = "New York";

  constructor(email: string, name: string) {
    this.email = email;
    this.name = name;
  }
}

const fernando = new User("gdg@gh.com", "fernando");

// fernando.city = "New York";