// Dados globais
let equipe = [];
let modalidades = [];

// Elementos DOM
const DOM = {
    tabelaBolsas: document.getElementById('tabela-bolsas').querySelector('tbody'),
    tabelaEquipe: document.getElementById('tabela-equipe').querySelector('tbody'),
    versaoEquipe: document.getElementById('versao-equipe'),
    totalEquipe: document.getElementById('total-equipe')
};

// Inicialização
document.addEventListener('DOMContentLoaded', async () => {
    await carregarDados();
    configurarEventos();
});

// Carrega os dados do JSON
async function carregarDados() {
    try {
        const response = await fetch('tabela_bolsas_ifes.json');
        if (!response.ok) throw new Error("Erro ao carregar dados");
        
        modalidades = await response.json();
        atualizarTabelaBolsas();
        console.log("Dados carregados com sucesso:", modalidades.length, "modalidades");
    } catch (error) {
        console.error("Erro ao carregar dados:", error);
        alert("Erro ao carregar dados das bolsas. Verifique o console.");
    }
}

// Atualiza a tabela de bolsas
function atualizarTabelaBolsas() {
    DOM.tabelaBolsas.innerHTML = modalidades.map(mod => `
        <tr>
            <td>${mod.Modalidade}</td>
            <td>${mod.Sigla}</td>
            <td>R$ ${mod.Valor.toFixed(2)}</td>
            <td>${mod.Teto}x</td>
        </tr>
    `).join('');
}

// Configura eventos da interface
function configurarEventos() {
    document.getElementById('adicionar').addEventListener('click', mostrarModalAdicionar);
    document.getElementById('remover').addEventListener('click', removerMembro);
    document.getElementById('limpar').addEventListener('click', limparEquipe);
    document.getElementById('importar').addEventListener('click', () => {
        document.getElementById('file-input').click();
    });
    document.getElementById('exportar').addEventListener('click', exportarEquipe);
    
    document.getElementById('file-input').addEventListener('change', handleFileImport);
}

// Mostra modal para adicionar membro
function mostrarModalAdicionar() {
    // Implementação do modal (pode usar um dialog HTML ou biblioteca como SweetAlert)
    const modalidade = prompt("Selecione a modalidade:");
    if (!modalidade) return;
    
    const chs = parseFloat(prompt("Carga Horária Semanal (CHS):", "8"));
    if (isNaN(chs)) return;
    
    const fatorX = parseFloat(prompt("Fator X:", "1.0"));
    if (isNaN(fatorX)) return;
    
    const mod = modalidades.find(m => m.Modalidade === modalidade);
    if (!mod) {
        alert("Modalidade não encontrada!");
        return;
    }
    
    if (fatorX > mod.Teto) {
        alert(`Fator X não pode ser maior que ${mod.Teto} para esta modalidade!`);
        return;
    }
    
    const valor = (mod.Valor * chs / 10) * fatorX;
    equipe.push({ 
        Modalidade: modalidade,
        CHS: chs,
        FatorX: fatorX,
        Valor: valor,
        Sigla: mod.Sigla
    });
    
    atualizarTabelaEquipe();
}

// Restante do código permanece igual...
// [Manter todas as outras funções do código anterior: atualizarTabelaEquipe, removerMembro, etc.]
