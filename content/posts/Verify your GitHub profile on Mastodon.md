---
title: Verify your GitHub profile on Mastodon
date: 2024-04-12T14:26:55+02:00
toc: true
---

---

## Special thanks

This article is inspired by [this post by Simon Willison](https://til.simonwillison.net/mastodon/verifying-github-on-mastodon), which I found through [this other post by Jeroen Mols](https://jeroenmols.com/blog/2022/11/26/mastodon-verify-github/), which I found through Google.

---

## Verification method

I was curious if it were possibile to verify one's GitHub profile page on Mastodon. Short answer: yes. Long answer: it's a little more convoluted than it really needs to be.

Mastodon's verification works by checking if the page you put on your Mastodon profile contains a link which redirects to your Mastodon profile. Specifically, Mastodon will look for either a `link` tag:

```html
<link href="https://mastodon.social/@username" rel="me">
```

Or an anchor tag:

```html
<a href="https://mastodon.social/@username" rel="me">Mastodon</a>
```

However, apparently, only the "URL" field on your GitHub profile accepts the important part, which is the [`rel="me"` microformat](https://microformats.org/wiki/rel-me). But I wanted that field to be for my blog, so I had to experiment.

Firstly, I thought that putting an anchor tag in my `MrVideo/README.md` repository, which is a special repo that lets GitHub users add a longer bio to their profile, would work. However, while the link is rendered correctly, the `rel="me"` property completely vanishes from your profile page.

A bit lost, I tried looking up online and stumbled upon the two posts I mentioned earlier. The way they verified their accounts was very smart: they created a new `.github.io` repository on their GitHub account and made a little, GitHub Pages powered website that only redirected visitors to their GitHub profile. I decided to do the same.

## My code

The code I used for my little static page looks like this:

```html
<html>
	<head>
		<meta charset="utf-8" />
		<title>Redirecting to my GitHub profile...</title>
		<link href="https://mastodon.social/@mrvideo" rel="me">
		<meta http-equiv="refresh" content="0; https://github.com/MrVideo">
	</head>
	<body />
</html>
```

A brief explanation of what this means:

- `<meta charset="utf-8" />` specifies the character encoding of the HTML file
- The second `meta` tag is used to simulate an HTTP response header (that's what `http-equiv` means) and is used to create an instant client redirect to my GitHub profile link (the `0` in the `content` field is the number of seconds to wait before the refresh)

So there you have it, this should verify your GitHub link on your Mastodon profile.

If you are currently using GitHub Pages to host your website and are using `username.github.io` as your URL, check out [Jeroen Mols's post](https://jeroenmols.com/blog/2022/11/26/mastodon-verify-github/) to see his solution.

## Problems

I have two main gripes with this method of verification:

- I would much rather be able to put the link directly on my GitHub profile somewhere than have to go through this
- Mastodon took an inexplicably long time to verify my `.github.io` page, while it took very little time to verify this blog

On the first issue, [some people think the same way I do](https://github.com/orgs/community/discussions/5720#discussioncomment-4035164).

I hope that, in the future, the folks at GitHub decide to add `rel="me"` properties automatically to their social links.

On the second issue, I am not sure whether it was I who did something wrong or if Mastodon just checks verifications at fixed times and I was farther away from the verification window the second time I tried to verify a link. This is not a problem however.