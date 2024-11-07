import streamlit as st

# Configurações iniciais
st.title("Gestão de Tarefas Diárias")
st.subheader("Acompanhe suas tarefas e veja o percentual de conclusão no final do dia!")

# Início da lista de tarefas
st.write("Insira suas tarefas diárias:")

# Armazena tarefas em uma lista
tasks = st.text_area("Digite suas tarefas separadas por vírgula:", placeholder="Exemplo: Tarefa 1, Tarefa 2, Tarefa 3")

# Cria uma lista a partir das tarefas digitadas
if tasks:
    task_list = [task.strip() for task in tasks.split(",") if task.strip()]

    # Exibe cada tarefa com um checkbox para marcar a conclusão
    st.write("Marque as tarefas concluídas:")
    completed_tasks = []
    for task in task_list:
        if st.checkbox(task):
            completed_tasks.append(task)

    # Calcula o percentual de conclusão
    total_tasks = len(task_list)
    completed_count = len(completed_tasks)
    completion_rate = (completed_count / total_tasks) * 100 if total_tasks > 0 else 0

    # Exibe o resultado
    st.write(f"Você completou {completed_count} de {total_tasks} tarefas.")
    st.write(f"Percentual de conclusão: {completion_rate:.2f}%")

# Sugestão para iniciar uma nova lista
st.write("---")
st.write("Para iniciar uma nova lista de tarefas, recarregue a página ou modifique o campo de tarefas.")

