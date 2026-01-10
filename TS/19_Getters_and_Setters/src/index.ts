class User {

  private _courseCount = 1;

  readonly city: string = "New York";
  constructor(
    public email: string,
    public name: string,
    // private userId: string
  ) {}

  private deleteToken() {
    console.log("Token deleted");
  }

  get getAppleEmail(): string {
    return `apple ${this.email}`;
  }

  get getCourseCount(): number {
    return this._courseCount;
  }

  set setCourseCount(courseCount : number) {
    if (courseCount <= 1) {
      throw new Error("Course count should be more than 1");
    }
    this._courseCount = courseCount;
  }
}

const fernando = new User("gdg@gh.com", "fernando");

// fernando.deleteToken();