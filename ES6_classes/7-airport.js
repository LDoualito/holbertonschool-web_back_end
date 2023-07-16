export default class Airport {
    constructor(name, string) {
      this._name = name;
      this._string = string;
    }
  
    get [Symbol.toStringTag]() {
      return this._string;
    }
  }
