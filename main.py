import flet as ft
import os
import sys
import asyncio
import subprocess


def open_program_directory():
    try:
        # 获取程序所在目录（支持脚本和打包后的exe）
        if getattr(sys, 'frozen', False):
            program_dir = os.path.dirname(sys.executable)
        else:
            program_dir = os.path.dirname(os.path.abspath(__file__))

        # 根据操作系统打开目录
        if sys.platform == "win32":
            subprocess.Popen(["explorer.exe", program_dir])
        elif sys.platform == "darwin":
            subprocess.Popen(["open", program_dir])
        else:
            subprocess.Popen(["xdg-open", program_dir])

        return True
    except Exception as e:

        return False


async def delayed_close(page):
    # 1. 先打开程序所在目录
    open_program_directory()

    # 2. 等待3秒
    await asyncio.sleep(2)

    # 3. 关闭窗口
    page.window.close()


def main(page: ft.Page):
    page.title = "白糖突然想到的U盘"
    page.window.height = 200
    page.window.width = 380
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.center()
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.bgcolor = ft.Colors.TRANSPARENT
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.always_on_top = True
    page.fonts = {"SourceHanSansSC": "SourceHanSansSC.otf"}
    page.theme = ft.Theme(font_family="SourceHanSansSC")

    window_title = ft.Text(
        "白糖突然想到的U盘",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="#1e1e1e"
    )

    # 标题栏区域
    title_bar = ft.WindowDragArea(
        ft.Container(
            ft.Row(
                [
                    window_title,
                    ft.Container(expand=True),
                ],
            ),
            padding=ft.padding.only(left=20, top=10, right=10, bottom=5)
        ),
    )

    # 图标和文字的水平布局
    icon_with_label = ft.Container(
        ft.Row(
            [
                ft.Image(
                    src="icon.png",
                    width=100,
                    height=100,
                    fit=ft.ImageFit.CONTAIN,
                    border_radius=ft.border_radius.all(8),
                ),
                ft.Text(
                    "正在启动...",
                    size=42,
                    weight=ft.FontWeight.W_500,
                    color="#1e1e1e",
                ),
            ],
            spacing=15,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(left=20, right=20, top=10, bottom=15),
    )

    # 整体布局
    card = ft.Container(
        ft.Column(
            [
                title_bar,
                ft.Divider(height=1, color="#e0e0e0"),
                icon_with_label,
            ],
            spacing=0,
        ),
        width=380,
        height=180,
        bgcolor=ft.Colors.WHITE,
        border_radius=28,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLACK12,
            offset=ft.Offset(0, 0)
        )
    )

    page.add(card)

    page.run_task(delayed_close, page)


if __name__ == "__main__":
    ft.app(target=main)