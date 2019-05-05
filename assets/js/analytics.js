;(function() {
    'use strict';

    var EVENTS = {
        ClickedNavLink: 'Clicked Nav Link',
        ClickedSocialLink: 'Clicked Social Link',
        IgnoreMe: 'Ignore Me'
    };

    var SELECTORS = {
        Nav: '#main-menu a',
        Social: '.avlanche-social a'
    };

    mixpanel.track_links(SELECTORS.Nav, EVENTS.ClickedNavLink);
    mixpanel.track_links(SELECTORS.Social, EVENTS.ClickedSocialLink);
})();
