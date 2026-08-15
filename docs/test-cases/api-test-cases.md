# API Test Cases

| ID | Scenario | Method | Endpoint | Expected |
|---|---|---|---|---|
| TC-001 | Get users | GET | /users | 200 + non-empty array |
| TC-002 | Get non-existing user | GET | /users/9999 | 404 |
| TC-003 | Get user with negative id | GET | /users/-1 | 404* |
| TC-004 | Get user with invalid id type | GET | /users/abc | 404* |
| TC-005 | Get users with trailing slash | GET | /users/ | 200 |
| TC-006 | Create user | POST | /users | 201 + generated id |

\* Based on observed JSONPlaceholder behavior; a production API should use its documented contract.
