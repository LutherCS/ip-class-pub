"use strict";

class Game {
  #title: string;
  #designer: string;
  #year: number;
  #review: string;

  constructor(title: string, designer: string, year: number, review: string) {
    this.#title = title;
    this.#designer = designer;
    this.#year = year;
    this.#review = review;
  }
  get title() {
    return this.#title;
  }
  get designer() {
    return this.#designer;
  }
  get year() {
    return this.#year;
  }
  get review() {
    return this.#review;
  }

  toString() {
    return `${this.#title} (${this.#year}) by ${this.#designer}`;
  }
  toJSON() {
    return {
      title: this.#title,
      designer: this.#designer,
      year: this.#year,
      review: this.#review,
    };
  }
}

class Shelf {
  #items: Array<Game>;
  #handlers: Array<Function>;

  constructor() {
    this.#items = [];
    this.#handlers = [];
  }

  subscribe(f: Function) {
    this.#handlers.push(f);
  }
  publish(msg: string, obj: Object | null) {
    for (let f of this.#handlers) {
      f(obj, msg);
    }
  }

  add(game: Game) {
    this.#items.push(game);
    this.save(`${game.title} has been added`);
  }

  remove(game: Game) {
    if (!this.#items.includes(game)) {
      throw new Error("Not found");
    }
    this.#items = this.#items.filter((item) => item != game);
    this.save(`${game.title} has been removed`);
  }

  save(message: string) {
    localStorage.setItem("myGames", JSON.stringify(this.#items));
    this.load(message);
  }

  load(message: string) {
    let localGames = localStorage.getItem("myGames");
    let parsedGames = localGames ? JSON.parse(localGames) : [];
    this.#items = [];
    for (let game of parsedGames) {
      this.#items.push(
        new Game(game.title, game.designer, game.year, game.review),
      );
    }
    this.publish(message, this);
  }

  *[Symbol.iterator]() {
    for (let item of this.#items) {
      yield item;
    }
  }
}
