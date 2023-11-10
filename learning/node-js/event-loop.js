// Node js

const fs = require("fs");
const crypto = require("crypto");

// initialize program
// execute top level code.
// required modules
// register callback function
// event loop start running

// 1. set timeout callback & callback queue
// 2. I/O polling callback & callback queue
// 3. set time immediate callback & callback queue
// 4. close callback & callback queue

// 1. set timeout callback queue
// process.nextTick callback queue
// micro task queue
// 2. I/O polling callback queue
// process.nextTick callback queue
// micro task queue
// 3. set time immediate callback queue
// process.nextTick callback queue
// micro task queue
// 4. close callback queue
// process.nextTick callback queue
// micro task queue

setImmediate(() => console.log("setImmediate 1 callback"));
setTimeout(() => console.log("setTimeout 1 callback"), 0);
const start = new Date();

// changes the thread pool size
// process.env.UV_THREADPOOL_SIZE = 10;
process.env.UV_THREADPOOL_SIZE = 4;

fs.readFile("./SampleCSVFile_556kb.csv", "utf-8", () => {
  console.log("I/O polling callback");
  console.log("-------");

  setTimeout(() => console.log("setTimeout 2 callback"), 0);
  setTimeout(() => console.log("setTimeout 3 callback"), 1000);
  setImmediate(() => console.log("setImmediate 2 callback"));

  process.nextTick(() => console.log("Process.nexttick callback"));

  //************ */
  // block the thread pool
  // use the sync callback
  //   crypto.pbkdf2Sync("password", "salt", 100000, 20000, "sha512");
  //   console.log(Date.now() - start, "password encryption 1");

  //   crypto.pbkdf2Sync("password", "salt", 100000, 20000, "sha512");
  //   console.log(Date.now() - start, "password encryption 2");
  //************ */

  //************ */
  // thread pool phase by default 4 threads are available
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 1 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 2 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 3 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 4 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 5 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 6 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 7 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 8 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 9 encryption")
  //   );
  //   crypto.pbkdf2("password", "salt", 100000, 2000, "sha512", () =>
  //     console.log(Date.now() - start, "password 10 encryption")
  //   );
  //************ */
});

// top level code execution first.
console.log("Top level code");
