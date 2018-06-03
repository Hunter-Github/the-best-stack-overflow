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
* No newsletters, [blog announcements](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change/), [job ads for shady companies](https://meta.stackoverflow.com/questions/332037/so-careers-should-stop-accepting-business-from-predatory-employers).

...and many, many more (including no Hot Network Questions)

## Minor stylistic improvements

* No more fixed top bar.

# Filters

```
! Disable HNQ - you want seamless experience without distractions 
stackoverflow.com###hot-network-questions

! No nagging newsletters
stackoverflow.com###newsletter-ad
stackoverflow.com##.newsletter-anon

! No Docs (defunct)
stackoverflow.com###nav-docs

! You have a nice job already, don't you?
stackoverflow.com###nav-jobs

! No login
stackoverflow.com##.btn-clear.login-link
stackoverflow.com##.btn.login-link

! No need to go through help while merely browsing
stackoverflow.com##.js-help-button.-link

! The community is mostly dead now
stackoverflow.com##.community-bulletin.module

! No answering
stackoverflow.com###post-form

! ADS!
stackoverflow.com###clc-tlb

! Legalese horsecrap in the footer steals your precious screenspace
stackoverflow.com###footer
stackoverflow.com##._short.js-footer.s-footer

! No thanks
stackoverflow.com##.special-status

! We don't need a hero. Leave it to Bonnie Tyler
stackoverflow.com##.s-hero

! This feature has been deleted because it's too chatty
stackoverflow.com###chat-feature

! Ugh.
stackoverflow.com##.js-dismissable.js-sample.js-experiment.unread-feature-notice.-feature-notice

! No loggin' in
stackoverflow.com##.btn-topbar-primary.login-link

! No bottom-feeders
stackoverflow.com###feed-link

! The infamous prison experiment
stackoverflow.com##.js-sample.js-experiment.unread-feature-notice.-feature-notice

! Ugh?
stackoverflow.com##.dno.js-feature-notice-dialog.feature-notice-dialog.topbar-dialog

! Really?
stackoverflow.com##.topbar-icon-on.js-experiment.unread-feature-notice.-feature-notice

! No sharing or editing
stackoverflow.com##.post-menu

! Comments are disabled.
stackoverflow.com##[id*="comments-link"]

! Screenspacesaver
stackoverflow.com##.bottom-notice

! ?!
stackoverflow.com##.btn-outlined

! No achievements
stackoverflow.com##.js-achievements-button.-link

! No inbox - we ain't logged in
stackoverflow.com##.js-inbox-button.-link

! Self-explanatory
stackoverflow.com##.everyonelovesstackoverflow

! Thanks but no thanks
stackoverflow.com###announcement-banner

! Temporary
stackoverflow.com##.quackoverflow

! Heroes are unboxable
stackoverflow.com###herobox

! My span is longer than yours
stackoverflow.com##.unread-feature-notice.-feature-notice > span

! The age of GDPR consent is long gone
stackoverflow.com###js-gdpr-consent-banner

! Make top bar not sticky - no need to reduce screen space!
stackoverflow.com##.top-bar._fixed:style(position: static !important)
```
