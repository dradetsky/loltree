from loltree import zsstree

def test_example():
    # XXX: TOKENIZATION FAIL
    #
    # the src lisp i got this example from is (roughly)
    #
    # (unless (getf vom::*config* :woo.signal)
    #   (vom:config :woo.signal :info))
    inp = ['start-multithread-server', [],
           ['unless', ['getf', 'vom::', '*config', '*', ':woo.signal'],
            ['vom:config', ':woo.signal', ':info']]]
    out = zsstree(inp)
    assert out.label == 'start-multithread-server'
    assert len(out.children) == 2
