#!/usr/bin/python

import os
import json

yummy_path = os.getenv("YUMMY_PATH")

bookmarks_dir = os.path.join(yummy_path, "Bookmarks")

def walkBookmark(bookmarkDir):

	ext = '.bkmk'
	bookmarks = []

	for (root, dirs, files) in os.walk(bookmarkDir):

		dirName = os.path.basename(root)

		for bkmk in list(filter(lambda f : f.endswith(ext), files)):
			
			bookmarks.append({
				"uid": dirName + "/" + bkmk[:-5],
				"type": "file",
				"title": bkmk[:-5],
				"arg": os.path.join(root, bkmk),
				"subtitle": dirName,
				"autocomplete": bkmk
				})

	return {"items": bookmarks}

print json.dumps(walkBookmark(bookmarks_dir))