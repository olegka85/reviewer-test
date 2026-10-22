<?php
/**
 * Reviewer video fixture: intentionally vulnerable WordPress example.
 * Not registered as a plugin and not executed in this repository.
 */
function reviewer_demo_wordpress_find_customer($wpdb, string $email) {
    // BUG: SQL injection; use $wpdb->prepare() in the repair step.
    return $wpdb->get_results(
        "SELECT id, email FROM {$wpdb->prefix}customers WHERE email = '$email'"
    );
}
