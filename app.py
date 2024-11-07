import streamlit as st
from datetime import datetime

# Configurações iniciais
st.title("Gestão de Tarefas Semanais")
st.subheader("Acompanhe suas tarefas diárias e veja o percentual de conclusão para cada dia da semana!")

# Lista predefinida de tarefas
task_list = [
    "Caminhar 5 mil passos",
    "Fazer alongamento",
    "Academia",
    "Expor ao sol",
    "Beber 1,5L de água pela manhã",
    "Beber 1,5L de água à tarde",
    "Meditação à noite",
    "Tomar suplementos"
]

# Lista de dias da semana
days_of_week = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

# Seletor de dia da semana
selected_day = st.selectbox("Selecione o dia da semana:", days_of_week)

# Inicializa o estado da sessão para armazenar as tarefas de cada dia
if "weekly_tasks" not in st.session_state:
    st.session_state.weekly_tasks = {day: [False] * len(task_list) for day in days_of_week}

# Exibe as tarefas com checkboxes para o dia selecionado
st.write(f"Tarefas para {selected_day}:")
completed_tasks = []
for i, task in enumerate(task_list):
    if st.checkbox(task, value=st.session_state.weekly_tasks[selected_day][i], key=f"{selected_day}_{i}"):
        completed_tasks.append(task)
        st.session_state.weekly_tasks[selected_day][i] = True
    else:
        st.session_state.weekly_tasks[selected_day][i] = False

# Calcula o percentual de conclusão para o dia selecionado
total_tasks = len(task_list)
completed_count = sum(st.session_state.weekly_tasks[selected_day])
completion_rate = (completed_count / total_tasks) * 100 if total_tasks > 0 else 0

# Exibe o resultado
st.write(f"Para {selected_day}, você completou {completed_count} de {total_tasks} tarefas.")
st.write(f"Percentual de conclusão: {completion_rate:.2f}%")

# Botão para salvar o progresso do dia
if st.button("Salvar progresso do dia"):
    st.success(f"Progresso para {selected_day} salvo com sucesso!")

# Exibe um resumo da semana
st.write("---")
st.write("Resumo da semana:")
for day in days_of_week:
    daily_completed_count = sum(st.session_state.weekly_tasks[day])
    daily_completion_rate = (daily_completed_count / total_tasks) * 100 if total_tasks > 0 else 0
    st.write(f"{day}: {daily_completed_count}/{total_tasks} tarefas concluídas - {daily_completion_rate:.2f}%")

