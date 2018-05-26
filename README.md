# the-best-stack-overflow
How to filter out advertisements and noise on Stack Overflow

# Prologue

Everybody likes reading [Stack Overflow](https://stackoverflow.com) (and, sometimes, other sites in the Stack Exchange network) to find solutions to their problems. However, there are dozens of irritating small items that hamper cognitive process. The solution? Install [uBlock Origin](https://github.com/gorhill/uBlock/releases) (optionally, [uMatrix](https://github.com/gorhill/uMatrix/releases)) and add cosmetic filters suggested below.

# Features

## You don't need to register as a user

* You should not risk [litigation](https://meta.stackexchange.com/questions/309746/a-new-2018-update-to-our-terms-of-service-is-here?noredirect=1) to read the site
* No need to submit to [capricious moderation](https://meta.stackoverflow.com/questions/368079/why-was-my-comment-removed-from-this-question?noredirect=1)

## You don't need to ask questions to enjoy solutions

* The fun of Stack Overflow used to be in answering questions. Nowadays, the management of the network looks to monetize experienced users, make them conform to their political agenda etc. etc.
* You are experienced enough to find your way through the docs on your own.

## No advertisements

* Stack Overflow is going to introduce ~~submarines~~ [native ads](https://meta.stackoverflow.com/questions/368378). While this feature is not implemented in the list (yet!), rest assured we will update the filters once the nasties are deployed.
* No newsletters, [blog announcements](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/), [job ads for shady companies](https://meta.stackoverflow.com/questions/332037/so-careers-should-stop-accepting-business-from-predatory-employers)

...and many, many more (including no Hot Network Questions)

# Filters

```
stackoverflow.com###hot-network-questions
stackoverflow.com###newsletter-ad
stackoverflow.com##.newsletter-anon
stackoverflow.com###nav-docs
stackoverflow.com###nav-jobs
stackoverflow.com##.btn-clear.login-link
stackoverflow.com##.btn.login-link
stackoverflow.com##.js-help-button.-link
stackoverflow.com##.community-bulletin.module
stackoverflow.com###post-form
stackoverflow.com###clc-tlb
stackoverflow.com###footer
stackoverflow.com##._short.js-footer.s-footer
stackoverflow.com##.special-status
stackoverflow.com##.s-hero
stackoverflow.com###chat-feature
stackoverflow.com##.js-dismissable.js-sample.js-experiment.unread-feature-notice.-feature-notice
stackoverflow.com##.btn-topbar-primary.login-link
stackoverflow.com###feed-link
stackoverflow.com##.js-sample.js-experiment.unread-feature-notice.-feature-notice
stackoverflow.com##.dno.js-feature-notice-dialog.feature-notice-dialog.topbar-dialog
stackoverflow.com##.topbar-icon-on.js-experiment.unread-feature-notice.-feature-notice
stackoverflow.com##.post-menu
stackoverflow.com##[id*="comments-link"]
stackoverflow.com##.bottom-notice
stackoverflow.com##.btn-outlined
stackoverflow.com##.js-achievements-button.-link
stackoverflow.com##.js-inbox-button.-link
stackoverflow.com##.everyonelovesstackoverflow
stackoverflow.com###announcement-banner
stackoverflow.com##.quackoverflow
stackoverflow.com###herobox
stackoverflow.com##.unread-feature-notice.-feature-notice > span
stackoverflow.com###js-gdpr-consent-banner
```
