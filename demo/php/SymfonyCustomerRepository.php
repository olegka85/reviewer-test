<?php
/**
 * Reviewer video fixture: intentionally vulnerable Symfony / Doctrine DBAL.
 * Not wired to any running Symfony application.
 */
namespace ReviewerDemo;

use Doctrine\DBAL\Connection;

final class SymfonyCustomerRepository
{
    public function findByEmail(Connection $connection, string $email): array
    {
        // BUG: SQL injection; use bound parameters in the repair step.
        return $connection->fetchAllAssociative(
            "SELECT id, email FROM customer WHERE email = '" . $email . "'"
        );
    }
}
