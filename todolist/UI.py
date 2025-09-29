from mcdreforged.api.rtext import *
from todolist.functions import functions as fun

prefix = '!!td'

help_head = """
================== §bToDoList §r==================
You can also input first chr of commands below, e.g. (§blist->l§r)
""".format(prefix=prefix)
help_body = {
    f"§b{prefix}": "§rshow help info",
    f"§b{prefix} list": "§rprint TODO list",
    f"§b{prefix} del <name>": "§rdelete <name>",
    f"§b{prefix} reload": "§rreload the plugin",
    f"§b{prefix} add <name> [<detail> <progress>]": "§radd/edit <name>, progress etc.",
    f"§b{prefix} tag": "§rlist all tags",
    f"§b{prefix} tag <tag>": "§rlist TODOs under <tag>",
    f"§b{prefix} tag add <name> <tag>": "§radd tag to <name>",
    f"§b{prefix} tag del <name> <tag>": "§rdelete tag for <name>",
}

wrong_command = f"§b[ToDoList]§4Incorrect command, §d!!td§4 for help"

def get_list(target_tag=""):
    c = ['']

    list_head = RText(f'================== §bToDoList §r==================').c(
        RAction.suggest_command, f'!!td list').h(f'§b!!td list')
    c.append(list_head)

    for name, list_info in fun.list_dic.items():
        tag_list = f''
        include = False
        for tag in fun.list_dic.get(name)["tags"]:
            if tag not in tag_list and tag != "defult":
                tag_list += f'{tag} '
            if tag == target_tag or target_tag =="":
                include = True
        if not include:
            continue
        list_msg = RTextList(
                            f'\n- ',
                            RText(f'[×] ', color = RColor.red).c(RAction.suggest_command, f'!!td del {name}')
                                .h(RText(f'delete', color = RColor.red)),
                            RText(f'[T+] ', color = RColor.green).c(RAction.suggest_command, f'!!td tag add {name} ')
                                .h(RText(f'add a tag', color = RColor.green)),
                                RText(f'[T-] ', color = RColor.red).c(RAction.suggest_command, f'!!td tag del {name} ')
                                .h(RText(f'delete a tag', color = RColor.red)),
                            RText(f'§b{name}').c(RAction.suggest_command, 
                                                f'!!td add {name} {fun.list_dic.get(name)["detail"][0]} {fun.list_dic.get(name)["progress"]}')
                            .h(
                                f'§rClick <name> to edit\n'
                                f'§7Latest editor:§6 {fun.list_dic.get(name)["creator"]}§7 Time:§6 {fun.list_dic.get(name)["time"]}',
                                f'\n§7Tag:§6 {tag_list}' if tag_list != "" else "",
                                f'\n§7Desciption:§6 {fun.list_dic.get(name)["detail"][0]}' if fun.list_dic.get(name)["detail"][0] !="" else "",
                                f'\n§7Progress:§6 {fun.list_dic.get(name)["progress"]}' if fun.list_dic.get(name)["progress"] !="" else ""
                            )
                        )
        c.append(list_msg)
    return c

def get_tags():
    c = []
    list_head = RText(f'================== §bToDoList-Tags §r==================').c(
        RAction.suggest_command, f'!!td tag').h(f'§b!!td tag')
    tag_list = RTextList()
    tag_list.append(list_head)
    tag_list.append(f'\n')
    for name, list_info in fun.list_dic.items():
        for tag in fun.list_dic.get(name)["tags"]:
            if tag not in c:
                c.append(tag)
    for ctag in c:
        tag_list.append((RText(f'§b<{ctag}> ').c(RAction.suggest_command,f'!!td tag {ctag}'))).h(f'Click to list this tag')
    return tag_list
