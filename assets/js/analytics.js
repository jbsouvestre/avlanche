var EVENTS = {
    ClickedNavLink: 'Clicked Nav Link',
    ClickedSocialLink: 'Clicked Social Link',
    IgnoreMe: 'Ignore Me'
};

mixpanel.track_links(
    '#main-menu a',
    EVENTS.ClickedNavLink
);

mixpanel.track_links(
    '.avlanche-social a',
    EVENTS.ClickedSocialLink
);
