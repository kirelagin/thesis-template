# vim: set filetype=python :

import os.path


def configure(conf):
    conf.load('tex')
    conf.load('pandoc', tooldir='.')

def build(bld):
    def make_sources(parts):
        sources = []
        for ch in parts:
            if isinstance(ch, basestring):
                sources.append(ch + '.pd')
            elif isinstance(ch, tuple):
                chdir = ch[0]
                sources.append(os.path.join(chdir, 'chapter.pd'))
                for sec in ch[1]:
                    sources.append(os.path.join(chdir, sec + '.pd'))
            else:
                raise TypeError('Wrong part')
        return ' '.join(os.path.join('text', s) for s in sources)
    sources = make_sources([
        'Introduction',
        ('Basics', [
            'Chapters',
            'Special',
            'Markdown',
            'Maths',
        ]),
        ('Floats', [
            'Listings',
            'Refs',
        ]),
        'Conclusion',
    ])

    bld(features='pandoc-merge', source=sources + ' bib.bib', target='text.latex',
            enabled_exts='smart raw_tex',
            disabled_exts='fancy_lists',
            flags='--pdf-engine=xelatex --listings --top-level-division=chapter',
            linkflags='--toc --listings --chapters -R')

    # Outputs main.pdf
    bld(features='tex', type='xelatex', source='main.latex', prompt=True)
    bld.add_manual_dependency(bld.bldnode.find_or_declare('main.pdf'),
                              bld.srcnode.find_node('utf8gost705u.bst'))
