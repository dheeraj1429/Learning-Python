const EventEmitter = require("events");

const myEmitter = new EventEmitter();

myEmitter.on("some-events", () => console.log("event function called"));
myEmitter.on("sale", (args) => {
  console.log(args);
});

myEmitter.emit("some-events");
myEmitter.emit("sale", { age: 20, place: "new delhi", height: 20 });
