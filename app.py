import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="SaaS Revenue & Churn Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

NAVY = '#1B3A6B'
DARK_NAVY = '#0F2240'
GOLD = '#C9922A'
MID_BLUE = '#2E5FA3'
GREEN = '#1E7B45'
RED = '#C0392B'
ORANGE = '#E67E22'
GRAY = '#4A5568'
WHITE = '#FFFFFF'
LIGHT_GRAY = '#F7F9FC'

st.markdown("""
    <style>
    .main { background-color: #F7F9FC; }
    .block-container { padding-top: 1rem; }
    .metric-card {
        background-color: white;
        border-radius: 8px;
        padding: 16px 20px;
        border-left: 4px solid #1B3A6B;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #0F2240;
    }
    .metric-label {
        font-size: 13px;
        color: #4A5568;
        margin-bottom: 4px;
    }
    .metric-delta {
        font-size: 12px;
        color: #1E7B45;
    }
    .section-header {
        font-size: 18px;
        font-weight: bold;
        color: #1B3A6B;
        border-bottom: 2px solid #C9922A;
        padding-bottom: 6px;
        margin-bottom: 16px;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    mrr = pd.read_csv('data/mrr_waterfall.csv')
    churn = pd.read_csv('data/churn_trend.csv')
    cohort = pd.read_csv('data/cohort_retention.csv')
    ltv = pd.read_csv('data/ltv_analysis.csv')
    nrr = pd.read_csv('data/nrr.csv')
    return mrr, churn, cohort, ltv, nrr

mrr_df, churn_df, cohort_df, ltv_df, nrr_df = load_data()

with st.sidebar:
    st.markdown(f"""
        <div style='background-color:{DARK_NAVY};
                    padding:20px;
                    border-radius:8px;
                    margin-bottom:20px;'>
            <h2 style='color:white; margin:0; font-size:18px;'>
                📊 SaaS Analytics
            </h2>
            <p style='color:#A8BEDC; margin:4px 0 0 0; font-size:12px;'>
                Revenue & Churn Intelligence
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Filters")

    period_filter = st.multiselect(
        "Select Period",
        options=['Normal', 'Stress Period', 'Recovery'],
        default=['Normal', 'Stress Period', 'Recovery']
    )

    tier_filter = st.multiselect(
        "Select Tier",
        options=['Starter', 'Growth', 'Enterprise'],
        default=['Starter', 'Growth', 'Enterprise']
    )

    st.markdown("---")
    st.markdown(f"""
        <div style='font-size:12px; color:{GRAY};'>
            <strong>Data:</strong> 24-month simulation<br>
            <strong>Period:</strong> Jan 2023 – Dec 2024<br>
            <strong>Built by:</strong> Tobou Egbekun<br>
            <strong>Stack:</strong> Python, BigQuery, Streamlit
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div style='background: linear-gradient(135deg, {DARK_NAVY}, {NAVY});
                padding: 28px 32px;
                border-radius: 10px;
                margin-bottom: 24px;
                border-bottom: 3px solid {GOLD};'>
        <h1 style='color: white; margin: 0; font-size: 26px;'>
            SaaS Revenue & Churn Analytics
        </h1>
        <p style='color: #A8BEDC; margin: 6px 0 0 0; font-size: 14px;'>
            24-Month Performance Report | Jan 2023 – Dec 2024 |
            Simulated SaaS Business
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='section-header'>Key Performance Indicators</div>",
    unsafe_allow_html=True
)

total_mrr_start = mrr_df['total_mrr'].iloc[0]
total_mrr_end = mrr_df['total_mrr'].iloc[-1]
mrr_growth = ((total_mrr_end - total_mrr_start) / total_mrr_start * 100)

avg_churn_normal = churn_df[
    churn_df['period_flag'] == 'Normal'
]['churn_rate_pct'].mean()

avg_churn_stress = churn_df[
    churn_df['period_flag'] == 'Stress Period'
]['churn_rate_pct'].mean()

healthy_months = nrr_df[nrr_df['nrr_status'] == 'Healthy'].shape[0]
total_months = len(nrr_df)

enterprise_ltv = ltv_df[
    ltv_df['tier'] == 'Enterprise'
]['ltv'].values[0]

starter_ltv = ltv_df[
    ltv_df['tier'] == 'Starter'
]['ltv'].values[0]

ltv_ratio = enterprise_ltv / starter_ltv

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-label'>Total MRR (Dec 2024)</div>
            <div class='metric-value'>${total_mrr_end:,.0f}</div>
            <div class='metric-delta'>↑ {mrr_growth:.1f}% since Jan 2023</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='metric-card'
             style='border-left-color:{RED};'>
            <div class='metric-label'>Stress Period Churn</div>
            <div class='metric-value'
                 style='color:{RED};'>{avg_churn_stress:.1f}%</div>
            <div class='metric-delta'
                 style='color:{RED};'>
                 {avg_churn_stress/avg_churn_normal:.1f}x normal rate
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='metric-card'
             style='border-left-color:{GOLD};'>
            <div class='metric-label'>Enterprise LTV</div>
            <div class='metric-value'
                 style='color:{NAVY};'>${enterprise_ltv:,.0f}</div>
            <div class='metric-delta'
                 style='color:{GOLD};'>
                 {ltv_ratio:.0f}x Starter LTV
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    nrr_color = GREEN if healthy_months >= 12 else GOLD
    st.markdown(f"""
        <div class='metric-card'
             style='border-left-color:{nrr_color};'>
            <div class='metric-label'>Healthy NRR Months</div>
            <div class='metric-value'
                 style='color:{nrr_color};'>
                 {healthy_months}/{total_months}
            </div>
            <div class='metric-delta'
                 style='color:{GRAY};'>
                 months above 100% NRR
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-header'>Monthly Recurring Revenue Waterfall</div>",
    unsafe_allow_html=True
)

fig_mrr = go.Figure()

fig_mrr.add_trace(go.Bar(
    x=mrr_df['month'],
    y=mrr_df['retained_mrr'],
    name='Retained MRR',
    marker_color=MID_BLUE,
    opacity=0.85
))

fig_mrr.add_trace(go.Bar(
    x=mrr_df['month'],
    y=mrr_df['new_mrr'],
    name='New MRR',
    marker_color=GREEN,
    opacity=0.85
))

fig_mrr.add_trace(go.Bar(
    x=mrr_df['month'],
    y=mrr_df['expansion_mrr'],
    name='Expansion MRR',
    marker_color=GOLD,
    opacity=0.85
))

fig_mrr.add_trace(go.Bar(
    x=mrr_df['month'],
    y=-mrr_df['churned_mrr'],
    name='Churned MRR',
    marker_color=RED,
    opacity=0.85
))

fig_mrr.add_vrect(
    x0='2024-02', x1='2024-06',
    fillcolor=RED, opacity=0.08,
    annotation_text='Stress Period',
    annotation_position='top left',
    annotation_font_color=RED
)

fig_mrr.update_layout(
    barmode='relative',
    height=420,
    plot_bgcolor=LIGHT_GRAY,
    paper_bgcolor=WHITE,
    font_color=GRAY,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ),
    yaxis=dict(
        tickprefix='$',
        tickformat=',.0f',
        gridcolor='#E2E8F0'
    ),
    xaxis=dict(gridcolor='#E2E8F0'),
    margin=dict(t=40, b=40, l=60, r=20)
)

st.plotly_chart(fig_mrr, use_container_width=True)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown(
        "<div class='section-header'>Churn Rate by Period</div>",
        unsafe_allow_html=True
    )

    filtered_churn = churn_df[
        churn_df['period_flag'].isin(period_filter)
    ]

    color_map = {
        'Normal': GREEN,
        'Stress Period': RED,
        'Recovery': ORANGE
    }

    fig_churn = px.bar(
        filtered_churn,
        x='month',
        y='churn_rate_pct',
        color='period_flag',
        color_discrete_map=color_map,
        labels={
            'churn_rate_pct': 'Churn Rate (%)',
            'month': 'Month',
            'period_flag': 'Period'
        }
    )

    fig_churn.add_hline(
        y=avg_churn_normal,
        line_dash='dash',
        line_color=GREEN,
        annotation_text=f'Normal avg: {avg_churn_normal:.1f}%',
        annotation_position='top right'
    )

    fig_churn.update_layout(
        height=360,
        plot_bgcolor=LIGHT_GRAY,
        paper_bgcolor=WHITE,
        font_color=GRAY,
        showlegend=True,
        margin=dict(t=20, b=40, l=60, r=20),
        yaxis=dict(gridcolor='#E2E8F0'),
        xaxis=dict(gridcolor='#E2E8F0', tickangle=45)
    )

    st.plotly_chart(fig_churn, use_container_width=True)

with col_right:
    st.markdown(
        "<div class='section-header'>Net Revenue Retention (NRR)</div>",
        unsafe_allow_html=True
    )

    nrr_color_map = {
        'Healthy': GREEN,
        'Warning': GOLD,
        'Critical': RED
    }

    fig_nrr = go.Figure()

    fig_nrr.add_trace(go.Scatter(
        x=nrr_df['month'],
        y=nrr_df['nrr_pct'],
        mode='lines+markers',
        line=dict(color=MID_BLUE, width=2.5),
        marker=dict(
            color=[nrr_color_map[s] for s in nrr_df['nrr_status']],
            size=8
        ),
        fill='tozeroy',
        fillcolor='rgba(46, 95, 163, 0.15)',
        name='NRR %'
    ))

    fig_nrr.add_hline(
        y=100,
        line_dash='dash',
        line_color=GREEN,
        annotation_text='100% threshold'
    )

    fig_nrr.add_hline(
        y=90,
        line_dash='dash',
        line_color=RED,
        annotation_text='90% floor'
    )

    fig_nrr.update_layout(
        height=360,
        plot_bgcolor=LIGHT_GRAY,
        paper_bgcolor=WHITE,
        font_color=GRAY,
        yaxis=dict(
            range=[80, 110],
            gridcolor='#E2E8F0',
            ticksuffix='%'
        ),
        xaxis=dict(
            gridcolor='#E2E8F0',
            tickangle=45
        ),
        margin=dict(t=20, b=40, l=60, r=20)
    )

    st.plotly_chart(fig_nrr, use_container_width=True)

st.markdown(
    "<div class='section-header'>Cohort Retention Heatmap</div>",
    unsafe_allow_html=True
)

cohort_pivot = cohort_df.pivot_table(
    index='cohort_month',
    columns='months_since_signup',
    values='retention_pct'
)

fig_cohort, ax = plt.subplots(figsize=(16, 5))
fig_cohort.patch.set_facecolor(WHITE)
ax.set_facecolor(LIGHT_GRAY)

sns.heatmap(
    cohort_pivot,
    ax=ax,
    cmap='RdYlGn',
    annot=True,
    fmt='.0f',
    linewidths=0.5,
    linecolor='white',
    vmin=0,
    vmax=100,
    cbar_kws={'label': 'Retention %'}
)

ax.set_title(
    'Customer Retention by Cohort — % Still Active',
    fontsize=13,
    fontweight='bold',
    color=DARK_NAVY,
    pad=12
)
ax.set_xlabel('Months Since Signup', color=GRAY)
ax.set_ylabel('Cohort Month', color=GRAY)
ax.tick_params(colors=GRAY)
plt.tight_layout()

st.pyplot(fig_cohort)

st.markdown(
    "<div class='section-header'>Customer Lifetime Value by Tier</div>",
    unsafe_allow_html=True
)

filtered_ltv = ltv_df[ltv_df['tier'].isin(tier_filter)]

fig_ltv = px.bar(
    filtered_ltv,
    x='tier',
    y='ltv',
    color='tier',
    color_discrete_map={
        'Enterprise': GREEN,
        'Growth': MID_BLUE,
        'Starter': GOLD
    },
    text='ltv',
    labels={
        'ltv': 'Lifetime Value ($)',
        'tier': 'Tier'
    }
)

fig_ltv.update_traces(
    texttemplate='$%{text:,.0f}',
    textposition='outside'
)

fig_ltv.update_layout(
    height=380,
    plot_bgcolor=LIGHT_GRAY,
    paper_bgcolor=WHITE,
    font_color=GRAY,
    showlegend=False,
    yaxis=dict(
        tickprefix='$',
        tickformat=',.0f',
        gridcolor='#E2E8F0'
    ),
    xaxis=dict(gridcolor='#E2E8F0'),
    margin=dict(t=40, b=40, l=60, r=20)
)

st.plotly_chart(fig_ltv, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='background-color:{DARK_NAVY};
                padding:20px 32px;
                border-radius:8px;
                border-top: 3px solid {GOLD};
                text-align:center;'>
        <p style='color:#A8BEDC; margin:0; font-size:13px;'>
            Built by <strong style='color:white;'>Tobou Egbekun</strong>
            — Analytics Engineer & Financial Modeler |
            Stack: Python · BigQuery · Streamlit |
            Data: 24-month SaaS simulation
        </p>
    </div>
""", unsafe_allow_html=True)