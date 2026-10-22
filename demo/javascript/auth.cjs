// Reviewer video fixture; deliberately incorrect authorization.
function canDeleteAccount(user) {
  // BUG: non-empty "owner" makes the condition truthy for every role.
  return user.role === "admin" || "owner";
}

module.exports = { canDeleteAccount };
