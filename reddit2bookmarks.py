import urllib2, cookielib, re
import ClientForm


class Bookmark:
    def __init__(self, url, name):
        self.url = url
        self.name=name

    def __repr__(self):
        print("%s  %s" % (self.name, self.url))

        
class RedditReader:

    bookmarks = list()
    def __init__(self, username, password):
        self.username= username    
        self.password = password
        self.url = 'http://www.reddit.com/saved'

        cookie_jar = cookielib.LWPCookieJar()
        cookie_jar = urllib2.HTTPCookieProcessor(cookie_jar)
        # debugger = urllib2.HTTPHandler(debuglevel=1)

        opener = urllib2.build_opener(cookie_jar)
        urllib2.install_opener(opener)


        response = urllib2.urlopen(self.url)
        forms = ClientForm.ParseResponse(response, backwards_compat=False)

        form = forms[1]
        try:
            form['user'] = self.username
            form['passwd'] = self.password
        except Exception, e:
            print('Got an error: \n"%s"' % e)
           
            exit()

        self.page = urllib2.urlopen(form.click()).read()

 
	#this didn't work
#pattern= re.compile("<a class=\"title loggedin \" href=\"http://(.+?)\" >(.+?)</a>&#32;<span class=\"domain\">(<a href=\"(.+?)\" >(.+?)</a>)</span></p><p class=\"tagline\">submitted&#32;1 hour&#32;ago&#32;by&#32;<a href=\"http://www.reddit.com/user/(.+?)\" class=\"author\" >(.+?)</a>&#32;to&#32;<a href=\"http://www.reddit.com/r/(.+?)/\" class=\"subreddit hover\" >(.+?)</a>");

	pattern= re.compile("<a class=\"title loggedin \" href=\"(http://[a-zA-Z0-9_\\.\\/\\-\\_\\=\\%\\?]+?)\" >(.+?)</a>&#32;<span class=\"domain\">\\(<a href=\".+?\" >(.+?)</a>\\)");
        links = pattern.findall(self.page)

        for link in links:
            bookmark1 = Bookmark(link[1], link[0]);
            print bookmark1.name;
            print bookmark1.url;
            bookmark1.__repr__()
            bookmarks.append(bookmark1);


if __name__ == '__main__':


    redditread = RedditReader(username, password)



