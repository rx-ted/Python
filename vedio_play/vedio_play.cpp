#include "vedio_play.h"

vedio_play::vedio_play(QObject *parent)
    : QAbstractItemModel(parent)
{
}

QVariant vedio_play::headerData(int section, Qt::Orientation orientation, int role) const
{
    // FIXME: Implement me!
}

QModelIndex vedio_play::index(int row, int column, const QModelIndex &parent) const
{
    // FIXME: Implement me!
}

QModelIndex vedio_play::parent(const QModelIndex &index) const
{
    // FIXME: Implement me!
}

int vedio_play::rowCount(const QModelIndex &parent) const
{
    if (!parent.isValid())
        return 0;

    // FIXME: Implement me!
}

int vedio_play::columnCount(const QModelIndex &parent) const
{
    if (!parent.isValid())
        return 0;

    // FIXME: Implement me!
}

QVariant vedio_play::data(const QModelIndex &index, int role) const
{
    if (!index.isValid())
        return QVariant();

    // FIXME: Implement me!
    return QVariant();
}
