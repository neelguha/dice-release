# Code describes knowledge graph object. We represent the knowledge graph as a list of 'triples', where each triple has 5 constituent parts:
#                           
#                                   (head, arc, tail, tail_type, source)
#
# Specifically, these are:
#   - head: the ID for the entity at the head of the triple (e.g. the subject)
#   - arc: the name of a relation/property (e.g. the predicate)
#   - tail: the value of the tail of the triple (e.g. the object). This could be an ID for another entity, or a value (e.g. float, string)
#   - tail_type: denotes whether the tail should be interpreted as an entity ID ('entity') or a float/string ('value')
#   - source: denotes the source of the triple (e.g. whether the triple came from Musicbrainz or Wikidata)

import os

class KG:


    def __init__(self, filepath):
        ''' Initialize KG object. 

        Args:
            filepath: path to directory with knowledge graph dataset 
        '''

        print("Loading data from %s..." % filepath)

        self.dir = filepath

        self.triples = []
        with open(os.path.join(self.dir, 'data', 'triples.txt')) as in_file:
            for line in in_file:
                items = line.strip().split("\t")
                self.triples.append(items)
        print("Loaded %d triples." % len(self.triples))

        self.tasks = {}

    def load_tasks(self):
        task_folders = [f.path for f in os.scandir(self.dir) if f.is_dir() ]    
        
        for folder in task_folders:
            task_name = folder.split("/")[-1]
            if task_name == 'data':
                continue 

            print("Task: %s" % task_name)
            self.tasks[task_name] = {}
            files = ['train.txt', 'valid.txt', 'test.txt']
            for file in files:
                X = []
                Y = []
                fpath = os.path.join(folder, file)
                if task_name == "category_prediction":
                    with open(fpath, 'r') as in_file:
                        for line in in_file:
                            items = line.strip().split(",")
                            X.append(items[0])
                            Y.append(items[1:])
                else:
                    with open(fpath) as in_file:
                        for line in in_file:
                            x, y = line.strip().split(",")
                            X.append(x)
                            Y.append(y)
                split = file.replace(".txt", "")
                print("%s (%s): %d samples" % (task_name, split, len(Y)))
                self.tasks[task_name][split] = {'X': X, 'Y': Y}
            print()
    
    def filter_triples(self, head_filter = [], arc_filter = [], tail_filter = [], etype_filter = [], source_filter = []):
        """ Returns a list of triples satisfying OR relation over criterion

        Args:
            head_filter (list): include all triples where the head entity is a member of head_filter
            arc_filter (list): include all triples where the arc is a member of arc_filter
            tail_filter (list): include all triples where the tail entity is a member of tail_filter
            etype_filter (list): include all triples where the tail entity type ("value" or "entity") is a member of etype_filter
            source_filter (list): include all triples where the source (e.g. musicbrainz) is a member of source_filter 

        Returns:
            filtered_triples: list of triples
        """
        
        # convert filter lists to dictionaries 
        head_filter = {k: 0 for k in head_filter}
        arc_filter = {k: 0 for k in arc_filter}
        tail_filter = {k: 0 for k in tail_filter}
        etype_filter = {k: 0 for k in etype_filter}
        source_filter = {k: 0 for k in source_filter}

        filtered = []
        for triple in self.triples:
            head, arc, tail, etype, source = triple

            if head in head_filter:
                filtered.append(triple)
                continue
            
            if arc in arc_filter:
                filtered.append(triple)
                continue
            
            if tail in tail_filter:
                filtered.append(triple)
                continue
            
            if etype in etype_filter:
                filtered.append(triple)
                continue
            
            if source in source_filter:
                filtered.append(triple)
                continue
        return filtered
