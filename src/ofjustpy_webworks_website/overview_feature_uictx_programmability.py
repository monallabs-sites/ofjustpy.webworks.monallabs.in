from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
oj.set_style("un")

with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_uictx_programmability_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Modular reusable codes using uictx namespaces "):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="text-center"):
                with H2(text="Programmatic constructs for webdev", classes="font-bold tracking-tight text-2xl"):
                    pass
            with Div(classes="flex flex-col  items-center mt-4"):
                with Ul(classes="space-y-2 text-balance text-lg text-slate-700 tracking-tight"):
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Define hierarchy of namespaces", classes="text-gray-700"):
                            pass
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Every active/mutable components  gets an access path within this hierarchy", classes="text-gray-700"):
                            pass                                        

                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Avoids circular name dependency issues in event handlers", classes="text-gray-700"):
                            pass

                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Facilitates code-reuse, modularity", classes="text-gray-700"):
                            pass                                        

                with Div(classes="text-left mt-4 ml-4"):
                    with H2(text="Code Demo: Using uictx namespace to construct a hierarchy over components", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="flex justify-center mt-2 font-bold text-sm tracking-tight overflow-auto") as code_block_container:
                    pass

                with Div(classes="text-left mt-4 ml-4"):
                    with H2(text="Code Demo: Access components globally via uictx hierarchy", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="flex justify-center mt-2 font-bold text-sm tracking-tight overflow-auto") as code_block_event_handler_container:
                    pass

            
from ofjustpy_plugins import format_code
code = """
with oj.uictx("mywp") as mywp:
   with oj.uictx("header") as headerctx:
      homelink = oj.AD.A(key="Home", target="http://www.mywebsite/Home", text="Home Page")
      deplink = oj.AD.A(key="Departments", target="http://www.mywebsite/DepartmentList")
      navlinks = oj.PD.StackH(childs = [homelink, deplink])
      header_panel = oj.PD.Subsection("Navigation Panel", childs=[navlinks])

   with oj.uictx("body") as bodyctx:
      bodytext = oj.PD.Prose(text="The body content of the webpage. This is placeholder.")
      body_panel = oj.PD.Subsection("Navigation Panel", cgens=[bodytext])
	  
   with oj.uictx("footer") as footerctx:
      content = oj.Mutable.Span(key="content", text="This is a placeholder for footer")
      footer_panel = oj.PD.Subsection(cgens=[content])
"""
fct = format_code(code)

code_block_container.components.append(fct)

code="""
   footer_content = mywp.footer.content.target
   footer_content.text = "Changed footer status"
"""

fct = format_code(code)
code_block_event_handler_container.components.append(fct)


