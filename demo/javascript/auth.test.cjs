// Run manually: node demo/javascript/auth.test.cjs
const assert = require("node:assert/strict");
const { canDeleteAccount } = require("./auth.cjs");

assert.equal(canDeleteAccount({ role: "viewer" }), false);
assert.equal(canDeleteAccount({ role: "admin" }), true);
console.log("JavaScript authorization checks passed");
