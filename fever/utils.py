
class JSONLineReader(Reader):
    def process(self,fp):
        data = []
        for line in fp.readlines():
            data.append(json.loads(line.strip()))
        return data




    def read_json(json_file,logging):
        logging.debug("inside read_json")
        l = []
        counter=0

        with open(json_file) as f:
            for eachline in (f):
                d = json.loads(eachline)
                a=d["data"]
                just_lemmas=' '.join(str(r) for v in a for r in v)
                l.append(just_lemmas)
                counter = counter + 1
        return l
