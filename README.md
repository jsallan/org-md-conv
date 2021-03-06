# org-md-conv

This is a python script to ease the migration from Emacs orgmode and org-roam to Logseq. 
## Reason for Migration to Logseq
On the one hand, I had a lot of fun learning the basics of Emacs and how to configure it for my needs. However, after a LOT of investment of time and energy, it's still not accessible on mobile and on occassion, I would accidentally hit a key combo that would cause me to lose what I had been recently typing. 

The point being, the skill and debugging required to use Emacs is significant. From my initial evaluation of Logseq spanning roughly 5 days, it appears to be much more accessible and uses transferable technology, e.g. CSS for formatting.
### Logseq using markdown
At this point, I've decided to use markdown as the format for Logseq.
- it's a transferrable language, i.e. proficiency in markdown might be useful elsewhere
- I like that headings are easy, i.e. # at the start of a line, and feel they will be useful for organizing notes.
### Summary
Compelling reasons to use Logseq over Emacs org-roam:
1. A mobile app that can be connected to the notes database using google Drive.
2. Lower barrier to entry and easier to maintain, meaning more time is spent note taking instead of fiddling.
3. A lower chance to lose recent writing.
4. Logseq uses technology that's applicable more broadly, i.e. markdown and CSS.
5. Logseq Plugins seem to be written in Typescript, which would be fun to learn.
## Implemented Migration Features
- converts orgmode headings to markdown/Logseq blocks
- converts orgmode lists to `shift-enter` in Logseq at the level of the orgmode heading that contained the list.