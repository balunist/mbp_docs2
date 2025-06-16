from pathlib import Path

import docutils.core

# from creole import html2rest
# from creole.rest2html.clean_writer import rest2html

if __name__ == "__main__":
    docutils.core.publish_file(
        source_path=F"{Path(__file__).parent.joinpath('source/usage/maplayout.html')}",
        destination_path=F"{Path(__file__).parent.joinpath('maplayout.rst')}",
        writer_name="html",
    )

    # with Path(__file__).parent.joinpath("mbpqs.html").open("r", encoding="utf-8") as f:
    #     lines = f.readlines()
    #     rest_out: list[str] = []
    #     for line in lines:
    #         txt: str = html2rest(line)
    #         rest_out.appenf(txt)

    #     for rest_line in rest_out:
    #         rest2html(rest_line, out_file=Path(__file__).parent.joinpath("mbpqs.rst"), append=True)
            