import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from router import Router  # 导入Router类
from dijkstra import dijkstra
from k_target_path import k_yen
from k_shortest_path import yen
from allpath import find_all_paths
from Q_Learning import Q_learning


def show_all_paths():
    all_paths_window = tk.Toplevel(root)
    all_paths_window.title("所有路径")

    start_label = tk.Label(all_paths_window, text="起点:")
    start_label.pack(pady=5)

    start_entry = tk.Entry(all_paths_window)
    start_entry.pack(pady=5)

    end_label = tk.Label(all_paths_window, text="终点:")
    end_label.pack(pady=5)

    end_entry = tk.Entry(all_paths_window)
    end_entry.pack(pady=5)

    result_text = tk.Text(all_paths_window, wrap=tk.WORD, height=10, width=40)
    result_text.pack(pady=10, padx=10)

    def calculate_all_paths():
        start_node = start_entry.get()
        end_node = end_entry.get()

        # Call the find_all_paths algorithm
        all_paths_result = find_all_paths(start_node, end_node)

        # Display the result in the Text widget
        result_text.delete("1.0", tk.END)  # Clear previous results

        if all_paths_result:
            result_text.insert(tk.END, f"找到的所有路径:\n")

            # Display each path in a new line
            for i, path in enumerate(all_paths_result):
                result_text.insert(tk.END, f"路径 {i + 1}: {' -> '.join(path)}\n")
        else:
            result_text.insert(tk.END, "无法找到符合条件的路径")

    calculate_button = tk.Button(all_paths_window, text="计算所有路径", command=calculate_all_paths)
    calculate_button.pack(pady=10)


def show_routing_options():
    routing_options_window = tk.Toplevel(root)
    routing_options_window.title("路由规划选项")

    def show_single_target_routing():
        routing_window = tk.Toplevel(root)
        routing_window.title("单目标路由")

        start_label = tk.Label(routing_window, text="起点:")
        start_label.pack(pady=5)

        start_entry = tk.Entry(routing_window)
        start_entry.pack(pady=5)

        end_label = tk.Label(routing_window, text="终点:")
        end_label.pack(pady=5)

        end_entry = tk.Entry(routing_window)
        end_entry.pack(pady=5)

        result_text = tk.Text(routing_window, wrap=tk.WORD, height=10, width=40)
        result_text.pack(pady=10, padx=10)

        def calculate_shortest_path():
            start_node = start_entry.get()
            end_node = end_entry.get()

            # Assuming you have a graph defined somewhere
            # Replace the following graph with your actual graph
            graph = {
                'A': {'B': 1, 'C': 4},
                'B': {'A': 1, 'C': 2, 'D': 5},
                'C': {'A': 4, 'B': 2, 'D': 1},
                'D': {'B': 5, 'C': 1}
            }

            # Call the dijkstra algorithm
            shortest_path_result = dijkstra(start_node, end_node)

            # Display the result in the Text widget
            result_text.delete("1.0", tk.END)  # Clear previous results
            result_text.insert(tk.END, f"最短路径: {' -> '.join(shortest_path_result)}")

        calculate_button = tk.Button(routing_window, text="计算最短路径", command=calculate_shortest_path)
        calculate_button.pack(pady=10)

    def show_multi_target_routing():
        routing_window = tk.Toplevel(root)
        routing_window.title("多目标路由")

        start_label = tk.Label(routing_window, text="起点:")
        start_label.pack(pady=5)

        start_entry = tk.Entry(routing_window)
        start_entry.pack(pady=5)

        middle_label = tk.Label(routing_window, text="中间结点:")
        middle_label.pack(pady=5)

        middle_entry = tk.Entry(routing_window)
        middle_entry.pack(pady=5)

        end_label = tk.Label(routing_window, text="终点:")
        end_label.pack(pady=5)

        end_entry = tk.Entry(routing_window)
        end_entry.pack(pady=5)

        result_text = tk.Text(routing_window, wrap=tk.WORD, height=10, width=40)
        result_text.pack(pady=10, padx=10)

        def calculate_shortest_path():
            start_node = start_entry.get()
            end_node = end_entry.get()
            middle_node = middle_entry.get()

            # Assuming you have a graph defined somewhere
            # Replace the following graph with your actual graph
            graph = {
                'A': {'B': 1, 'C': 4},
                'B': {'A': 1, 'C': 2, 'D': 5},
                'C': {'A': 4, 'B': 2, 'D': 1},
                'D': {'B': 5, 'C': 1}
            }

            # Call the dijkstra algorithm
            shortest_path_result = k_yen(start_node, end_node, middle_node)

            # Display the result in the Text widget
            result_text.delete("1.0", tk.END)  # Clear previous results
            result_text.insert(tk.END, f"待选路径: {shortest_path_result}")

        calculate_button = tk.Button(routing_window, text="计算最短路径", command=calculate_shortest_path)
        calculate_button.pack(pady=10)

    def show_multi_path_routing():
        routing_window = tk.Toplevel(root)
        routing_window.title("多路径路由")

        start_label = tk.Label(routing_window, text="起点:")
        start_label.pack(pady=5)

        start_entry = tk.Entry(routing_window)
        start_entry.pack(pady=5)

        end_label = tk.Label(routing_window, text="终点:")
        end_label.pack(pady=5)

        end_entry = tk.Entry(routing_window)
        end_entry.pack(pady=5)

        k_num = tk.Label(routing_window, text="路径数目:")
        k_num.pack(pady=5)

        k_num_entry = tk.Entry(routing_window)
        k_num_entry.pack(pady=5)

        result_text = tk.Text(routing_window, wrap=tk.WORD, height=10, width=40)
        result_text.pack(pady=10, padx=10)

        def calculate_shortest_path():
            start_node = start_entry.get()
            end_node = end_entry.get()
            k_num = k_num_entry.get()

            # Assuming you have a graph defined somewhere
            # Replace the following graph with your actual graph
            graph = {
                'A': {'B': 1, 'C': 4},
                'B': {'A': 1, 'C': 2, 'D': 5},
                'C': {'A': 4, 'B': 2, 'D': 1},
                'D': {'B': 5, 'C': 1}
            }

            # Call the dijkstra algorithm
            shortest_path_result = yen(start_node, end_node, int(k_num))

            # Display the result in the Text widget
            result_text.delete("1.0", tk.END)  # Clear previous results
            result_text.insert(tk.END, f"待选路径: {shortest_path_result}")

        calculate_button = tk.Button(routing_window, text="计算最短路径", command=calculate_shortest_path)
        calculate_button.pack(pady=10)

    def show_dynamic_routing():
        routing_window = tk.Toplevel(root)
        routing_window.title("动态路由")

        result_text = tk.Text(routing_window, wrap=tk.WORD, height=10, width=40)
        result_text.pack(pady=10, padx=10)

        def calculate_shortest_path():
            # Assuming you have a graph defined somewhere
            # Replace the following graph with your actual graph
            graph = {
                'A': {'B': 1, 'C': 4},
                'B': {'A': 1, 'C': 2, 'D': 5},
                'C': {'A': 4, 'B': 2, 'D': 1},
                'D': {'B': 5, 'C': 1}
            }

            # Call the dijkstra algorithm
            shortest_path_result = Q_learning()

            # Display the result in the Text widget
            result_text.delete("1.0", tk.END)  # Clear previous results
            result_text.insert(tk.END, f"训练结果: {shortest_path_result}")

        calculate_button = tk.Button(routing_window, text="计算最短路径", command=calculate_shortest_path)
        calculate_button.pack(pady=10)

    single_target_button = tk.Button(routing_options_window, text="单目标路由", command=show_single_target_routing)
    single_target_button.pack(pady=10)

    multi_target_button = tk.Button(routing_options_window, text="多目标路由", command=show_multi_target_routing)
    multi_target_button.pack(pady=10)

    multi_path_button = tk.Button(routing_options_window, text="多路径路由", command=show_multi_path_routing)
    multi_path_button.pack(pady=10)

    dynamic_routing_button = tk.Button(routing_options_window, text="动态路由规划", command=show_dynamic_routing)
    dynamic_routing_button.pack(pady=10)


def show_topology_network():
    try:
        image_path = "Figure_1.png"  # 替换为你的拓扑网络图路径
        image = Image.open(image_path)
        topology_window = tk.Toplevel(root)
        topology_window.title("拓扑网络")

        # 将图片转换为Tkinter的PhotoImage对象
        tk_image = ImageTk.PhotoImage(image)

        # 创建Label来显示图像
        image_label = tk.Label(topology_window, image=tk_image)
        image_label.image = tk_image
        image_label.pack()

    except Exception as e:
        messagebox.showerror("错误", f"无法加载拓扑网络图: {e}")


def show_landmark_query():
    landmark_query_window = tk.Toplevel(root)
    landmark_query_window.title("路标查询")

    def perform_query():
        landmark_name = entry.get()
        router_instance = get_router_instance(landmark_name)

        if router_instance:
            display_information(router_instance)
        else:
            messagebox.showwarning("警告", f"未找到路标节点：{landmark_name}")

    def get_router_instance(landmark_name):
        try:
            from router import router_instances

            # 使用字典获取Router对象
            return router_instances.get(landmark_name)
        except ImportError:
            return None

    def display_information(router_instance):
        information_window = tk.Toplevel(landmark_query_window)
        information_window.title("节点信息")

        text = tk.Text(information_window, wrap=tk.WORD, height=10, width=40)
        text.pack(pady=10, padx=10)

        if router_instance:
            # 获取Router对象的信息并显示在Text组件中
            information = f"节点序号: {router_instance.sign}\n节点名称: {router_instance.name}\n"
            information += f"物资需求: {router_instance.requirement}\n节点容量: {router_instance.datasize}\n"
            information += f"是否可达: {router_instance.is_accessible}\n"

            text.insert(tk.END, information)
        else:
            messagebox.showwarning("警告", "未找到对应路标节点")

    label = tk.Label(landmark_query_window, text="请输入想要查询的路标节点名称：")
    label.pack(pady=10)

    entry = tk.Entry(landmark_query_window)
    entry.pack(pady=10)

    query_button = tk.Button(landmark_query_window, text="查询", command=perform_query)
    query_button.pack(pady=10)


def on_exit():
    if messagebox.askyesno("退出", "确定要退出程序吗？"):
        root.destroy()



# 创建主窗口
root = tk.Tk()
root.title("无人机路由系统")

# 设置整体界面的样式
style = ttk.Style()
style.configure('TButton', padding=(20, 10), font=('Helvetica', 14))

# 设置主窗口的大小
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# 添加标签
label = tk.Label(root, text="无人机路由规划", font=("Helvetica", 16))
label.pack(pady=20)





routing_button = ttk.Button(root, text="全部路径", command=show_all_paths)
routing_button.pack(pady=10)

routing_button = ttk.Button(root, text="路由规划", command=show_routing_options)
routing_button.pack(pady=10)

topology_button = ttk.Button(root, text="拓扑网络", command=show_topology_network)
topology_button.pack(pady=10)

landmark_query_button = ttk.Button(root, text="路标查询", command=show_landmark_query)
landmark_query_button.pack(pady=10)

exit_button = ttk.Button(root, text="退出", command=on_exit)
exit_button.pack(pady=10)

# Add frames for better organization
frame_routing = ttk.Frame(root)
frame_routing.pack(pady=10)

label = tk.Label(frame_routing, text="无人机路由规划", font=("Helvetica", 16))
label.pack(pady=10)

routing_button = ttk.Button(frame_routing, text="全部路径", command=show_all_paths)
routing_button.pack(pady=5)

routing_button = ttk.Button(frame_routing, text="路由规划", command=show_routing_options)
routing_button.pack(pady=5)

frame_other = ttk.Frame(root)
frame_other.pack(pady=10)

topology_button = ttk.Button(frame_other, text="拓扑网络", command=show_topology_network)
topology_button.pack(pady=5)

landmark_query_button = ttk.Button(frame_other, text="路标查询", command=show_landmark_query)
landmark_query_button.pack(pady=5)

exit_button = ttk.Button(frame_other, text="退出", command=on_exit)
exit_button.pack(pady=5)

'''
# 添加按钮
routing_button = ttk.Button(root, text="全部路径", command=show_all_paths)
routing_button.pack(pady=15)

routing_button = ttk.Button(root, text="路由规划", command=show_routing_options)
routing_button.pack(pady=15)

topology_button = ttk.Button(root, text="拓扑网络", command=show_topology_network)
topology_button.pack(pady=15)

landmark_query_button = ttk.Button(root, text="路标查询", command=show_landmark_query)
landmark_query_button.pack(pady=15)

exit_button = ttk.Button(root, text="退出", command=on_exit)
exit_button.pack(pady=15)
'''
# 运行主循环
root.mainloop()